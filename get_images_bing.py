#!/usr/bin/env python3

import sys
import os

# from google_images_download import google_images_download
from bing_image_downloader import downloader
from PIL import Image


def download_images(qry_list, limit=100, output_dir="image_data"):
    """Download images to folder."""
    output_folders = []

    for qry in qry_list:
        qry_string = qry.strip()
        print(f"Downloading {qry_string}")
        qry_output_folder = os.path.join(output_dir, qry_string)
        downloader.download(qry_string, limit=limit, output_dir=output_dir, timeout=60)
        output_folders.append(qry_output_folder)

    return output_folders


# def resize_image(im):
#     return im.resize((150, 150))


# def correct_image_types(paths):
#     """Fix image types.
#
#     Remove original files
#     Convert webp to jpg
#     """
#     for keyword in paths:
#         for image_file in paths[keyword]:
#             if image_file.endswith(".webp"):
#                 print(f"Fixing: {image_file}")
#                 im = Image.open(image_file).convert("RGB")
#                 im.save(image_file + "_fix.jpg", "jpeg")
#                 os.remove(image_file)

def main(args):
    qry_list = args[1].split(',')
    output_folders = download_images(qry_list, limit=5)
    print(output_folders)
    # correct_image_types(paths)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print("Error: Invalid parameters")
        print('get_images.py "cat1,cat2,cat3')
