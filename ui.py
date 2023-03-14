"""This module creates a window that allows users to select parameters more
easily. NOT YET FUNCTIONAL

Contains:

    * :func:`main`
"""

import PySimpleGUI as psg
import create


# set theme
psg.theme('DarkBrown1')

# define window elements
L_F1 = [[psg.Frame('Hidden Image/Frame 1', [
          [psg.Input(k='f1'), psg.FileBrowse()]
        ])]]
"""UI elements for selecting frame 1."""
L_F2 = [[psg.Frame('Hidden Image/Frame 2', [
          [psg.Input(k='f2'), psg.FileBrowse()]
       ])]]
"""UI elements for selecting frame 2."""
L_GO = [[psg.Frame('Output', [
          [psg.Input(k='filename'),psg.Text('.png')],
          [psg.Button('Create', k='go'), psg.Text(k='status')]
       ])]]
"""UI elements for triggering generation."""
L_INFO = [[psg.StatusBar('github.com/gavboi', justification='c')]]
"""UI elements for window information."""


def display_status(status):
    """Updates status text in window.

    :param status: text to insert
    :type status: str
    """

    win['status'].update(status)


layout = L_F1 + L_F2 + L_GO + L_INFO
win = psg.Window('Short APNG', layout)
while True:
    event, values = win.read()
    if event in (psg.WIN_CLOSED, 'Exit'):
        break
    if event == 'go':
        if not create.verify_image(values['f1']):
            display_status('Image 1 not valid!')
            continue
        if not create.verify_image(values['f2']):
            display_status('Image 2 not valid!')
            continue
        filename = 'out' if values['filename'] == '' else values['filename']
        if (create.make_apng(values['f1'], values['f2'], 'out') if
            filename == '' else
            create.make_apng(values['f1'], values['f2'], filename)):
                display_status(filename + '.png created.')
        else:
            display_status('File unable to be created.')
win.close()


