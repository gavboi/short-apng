"""This module creates a window that allows users to select parameters more
easily. NOT YET FUNCTIONAL

Contains:

    * :func:`main`
"""

import PySimpleGUI as psg
from PIL import Image
import create


# set theme
psg.theme('DarkBrown1')

# define window elements
L_F1 = [[psg.Frame('Hidden Image/Frame 1', [
          [psg.Input(k='i1', change_submits=True), psg.FileBrowse()]
        ], k='f1')]]
"""UI elements for selecting frame 1."""
L_F2 = [[psg.Frame('Hidden Image/Frame 2', [
          [psg.Input(k='i2', change_submits=True), psg.FileBrowse()]
       ], k='f2')]]
"""UI elements for selecting frame 2."""
L_GO = [[psg.Frame('Output', [
          [psg.Input(k='filename', change_submits=True),psg.Text('.png')],
          [psg.Checkbox('Allow resizing', k='resize')],
          [psg.Button('Create', k='go'), psg.Text(k='status')]
       ], k='fo')]]
"""UI elements for triggering generation."""
L_INFO = [[psg.StatusBar('github.com/gavboi', justification='c')]]
"""UI elements for window information."""
L_SPACER = [[psg.Text(k='spacer', pad=(0,0), font='Any 1')]]
"""UI elements for window information."""


def display_status(status):
    """Updates status text in window.

    :param status: text to insert
    :type status: str
    """

    win['status'].update(status)


layout = L_F1 + L_F2 + L_GO + L_SPACER + L_INFO
win = psg.Window('Short APNG', layout, resizable=True, finalize=True)
win['f1'].expand(True, False, False)
win['i1'].expand(True, False, False)
win['f2'].expand(True, False, False)
win['i2'].expand(True, False, False)
win['fo'].expand(True, False, False)
win['filename'].expand(True, False, False)
win['spacer'].expand(False, True, True)
size = (0,0)
while True:
    event, values = win.read()
    if event in (psg.WIN_CLOSED, 'Exit'):
        break
    if event == 'go':
        # verify first input
        if not create.verify_image(values['i1']):
            display_status('Image 1 not valid!')
            continue
        # note size of first image
        with Image.open(values['i1']) as im:
            size = im.size
        # verify second input
        if not create.verify_image(values['i2']):
            display_status('Image 2 not valid!')
            continue
        # check if sizes match, if needed fix it
        i2 = values['i2']
        if not create.verify_image(values['i2'], size):
            if values['resize']:
                with Image.open(i2) as im:
                    im_resized = im.resize(size)
                    i2 = i2[:-4] + '_resize.png' 
                    im_resized.save(i2)
            else:
                display_status('Image sizes do not match!')
                continue
        filename = 'out' if values['filename'] == '' else values['filename']
        if create.make_apng(values['i1'], i2, filename):
            display_status(filename + '.png created.')
        else:
            display_status('File unable to be created.')
    elif event in ('i1', 'i2', 'filename'):
        display_status('')
win.close()


