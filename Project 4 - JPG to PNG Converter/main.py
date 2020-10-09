"""
This module implements the convert an image from JPG to PNG exercise of the Section 17 of the course.
"""

import os
import sys

from PIL import Image


def convert_image(path, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for filename in os.listdir(path):
        clean_name = os.path.splitext(filename)[0]
        img = Image.open(f'{path}{filename}')

        # Added the / in case user doesn't enter it. You may want to check for this and add or remover it.
        img.save(f'{directory}/{clean_name}.png', 'png')

        print('Image converted!')


# Entry point of the script
if __name__ == '__main__':
    # Read arguments
    arg_path = sys.argv[1]
    arg_directory = sys.argv[2]

    # Call the convert image function
    convert_image(arg_path, arg_directory)
