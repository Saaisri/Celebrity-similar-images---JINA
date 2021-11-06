import streamlit as st
import random
import os
from config import image_endpoint, text_endpoint, top_k, images_path
from helper import search_by_file, search_by_text, UI, create_temp_file

endpoint = image_endpoint
matches = []

# Layout
st.set_page_config(page_title="Jina meme search")
st.markdown(
    body=UI.css,
    unsafe_allow_html=True,
)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row; margin-left:auto; margin-right: auto; align: center}</style>', unsafe_allow_html=True)
# Sidebar
st.sidebar.header("Media type")
st.sidebar.markdown(UI.text_block, unsafe_allow_html=True)
st.sidebar.markdown(UI.image_repo_block, unsafe_allow_html=True)

st.markdown(UI.repo_banner, unsafe_allow_html=True)

st.header("What do you want to search with?")
media_type = st.radio("", ["Image", "Nothing"])

if media_type == "Image":
    # st.header("Search from your own image...")
    upload_cell, preview_cell = st.columns([12, 1])
    query = upload_cell.file_uploader("")
    if query:
        uploaded_image = create_temp_file(query)
        preview_cell.image(uploaded_image)
        if st.button(label="Search"):
            if not query:
                st.markdown("Please enter a query")
            else:
                matches = search_by_file(image_endpoint, top_k, "/tmp/query.png")

    # Sample image list
    # elif media_type == "Text":
        # st.header("...or search from an existing meme")
        # sample_files = []
        # for filename in os.listdir("./samples"):
            # sample_files.append(filename)
        # sample_cells = st.columns(len(sample_files))

        # for cell, filename in zip(sample_cells, sample_files):
            # meme_name = filename.split(".")[0]
            # cell.image(f"samples/{filename}", width=128)
            # if cell.button(f"{meme_name}", key=meme_name):
                # matches = search_by_file(image_endpoint, top_k, f"samples/{filename}")
# elif media_type == "Text":
#     # st.subheader("Search with a meme subject and/or caption...")
#     query = st.text_input("", key="text_search_box")
#     search_fn = search_by_text
#     if st.button("Search", key="text_search"):
#         matches = search_by_text(query, text_endpoint, top_k)
#     st.subheader("...or search from a sample")
#     sample_texts = [
#         "squidward school",
#         "so you're telling me willy wonka",
#         "seagull kitkat",
#     ]
#     for text in sample_texts:
#         if st.button(text):
#             matches = search_by_text(text, text_endpoint, top_k)
# else:
    st.markdown(
        """
### 
1. The [dataset we're using](https://www.kaggle.com/jessicali9530/celeba-dataset) only contains so many "celebrity images"
2. This time round we only indexed 1,000 celebrity images from the shuffled dataset. So there's a chance that even if a image exists in the dataset, it didn't get picked up in our subset.

Update: Image search still at 1,000 for now.

### So just index more images, duh!
We didn't expect this to explode so soon. We're doing this as we speak.

### Ugh, just use a better dataset
We use this dataset because it has rich metadata. That lets use image search

### My celebrity image search is much better!

Awesome! We threw this together quickly and didn't expect it to blow up. With more time we would use a better image encoder (like CLIP) and probably throw in some OCR too.

"""
    )

# Results area
cell1, cell2, cell3 = st.columns(3)
cell4, cell5, cell6 = st.columns(3)
cell7, cell8, cell9 = st.columns(3)
all_cells = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]

for cell, match in zip(all_cells, matches):
    if media_type == "Text":
        cell.image("http:" + match["tags"]["image_url"])
    else:
        # cell.image(match["tags"]["uri_absolute"], use_column_width="auto")
        cell.image(match["tags"]["uri"], use_column_width="auto")

