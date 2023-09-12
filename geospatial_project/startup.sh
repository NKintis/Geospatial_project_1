#!/bin/bash

echo "Starting the startup.sh script..."

echo "Starting image_download_input.py..."

python image_download_input.py &

bg_process_pid=$!

wait $bg_process_pid

echo "image_download_input.py completed successfully. Starting s2_preprocess.py..."

python s2_preprocess.py

echo "s2_preprocess.py completed successfully."

jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
