#!/bin/bash

URL="kaggle kernels output vinayakshanawad/celebrity-face-recognition-vggface-model -p /path/to/dest"
OUTPUT_DIR="./data"
OUTPUT_FILENAME=$OUTPUT_DIR/memes.json

mkdir -p $OUTPUT_DIR

wget -O $OUTPUT_FILENAME $URL
