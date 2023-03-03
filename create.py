from apng import APNG
from os.path import isfile

def verify_image(img):
    if img:
        return isfile(img)
    return False

def make_apng(preview=None, hidden=None, filename=None):

    while not verify_image(preview):
        preview = input('Input path to preview image/frame 1: ')
    while not verify_image(hidden):
        hidden = input('Input path to hidden image/frame 2: ')
    while not filename:
        filename = input('Input name of output file (no extension): ')

    im = APNG(num_plays=1)
    im.append_file(preview, delay=1)
    im.append_file(hidden, delay=1)
    im.save(filename + '.png')
    print("File created")

if __name__ == '__main__':
    make_apng()

