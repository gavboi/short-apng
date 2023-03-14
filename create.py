"""This module allows interaction with files to merge them into an APNG.

This module can be run as the primary file, or called from another.

Contains:

    * :func:`verify_image`
    * :func:`make_apng`
"""

from apng import APNG
from os.path import isfile
from PIL import Image

VALID_IMAGES = ('.png','.jpg')
"""File extensions of valid images to use."""


def verify_image(img, size=None):
    """Checks if a path leads to an image suitable for the APNG.

    :param img: path to check
    :type img: str
    :param size: size to enforce
    :type size: (int, int)
    :return: `True` if path leads to suitable image, else `False`
    :rtype: bool
    """
    
    if img:
        if (isfile(img) and
            len(img) > 4 and
            img[-4:] in VALID_IMAGES):
                if size:
                    with Image.open(img) as im:
                        return size == im.size
                else:
                    return True
    return False


def make_apng(frame1=None, frame2=None, filename=None):
    """Creates APNG from parameters. If parameters not given, will prompt user
    to input them at runtime.

    :param frame1: the path to the image for frame 1
    :type frame1: str
    :param frame2: the path to the image for frame 2
    :type frame2: str
    :param filename: the name of the PNG file to be created
    :type filename: str
    :return: `True` if PNG file created, else `False`
    :rtype: bool
    """

    # verify inputs are valid
    while not verify_image(frame1):
        frame1 = input('Input path to preview image/frame 1: ')
    while not verify_image(frame2):
        frame2 = input('Input path to hidden image/frame 2: ')
    while not filename:
        filename = input('Input name of output file (no extension): ')

    # make png
    im = APNG(num_plays=1)
    im.append_file(frame1, delay=1)
    im.append_file(frame2, delay=1)
    name = filename + '.png'
    im.save(name)
    if isfile(name):
        print("File created")
        return True
    else:
        print("Something went wrong")
        return False


# if running this file directly, call make_apng
if __name__ == '__main__':
    make_apng()

