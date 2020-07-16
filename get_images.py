#!/usr/bin/env python3

import sys
import os

from google_images_download import google_images_download
from PIL import Image


def download_images(pos_img, neg_img, limit=100, output_dir="image_data"):
    """Download images to folder."""
    response = google_images_download.googleimagesdownload()

    arguments = {
        "keywords": f"{pos_img},{neg_img}",
        "limit": limit,
        "print_urls": False,
        "output_directory": output_dir,
    }
    paths = response.download(arguments)
    return paths


def resize_image(im):
    return im.resize((150, 150))


def correct_image_types(paths):
    """Fix image types.

    Remove original files
    Convert webp to jpg
    """
    for keyword in paths:
        for image_file in paths[keyword]:
            if image_file.endswith(".webp"):
                print(f"Fixing: {image_file}")
                im = Image.open(image_file).convert("RGB")
                im.save(image_file + "_fix.jpg", "jpeg")
                os.remove(image_file)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        paths, _ = download_images(sys.argv[1], sys.argv[2])
        correct_image_types(paths)
    else:
        print("Error: Invalid parameters")
        print('get_images.py "<positive category>" "<negative category"')
