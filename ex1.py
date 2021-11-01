from jina import DocumentArray
from jina.types.document.generators import from_files

da = (
    DocumentArray(from_files(''))
    .convert_uri_to_image_blob()
    .set_image_blob_size(224, 224)
    .set_image_blob_normalization()
    .set_image_blob_channel_axis(-1, 0)
)

print(d.blob)
print(d.blob.shape)