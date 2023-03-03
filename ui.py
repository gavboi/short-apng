"""This module creates a window that allows users to select parameters more
easily. NOT YET FUNCTIONAL

Contains:

    * :func:`main`
"""

import PySimpleGUI as psg


# set theme
psg.theme('DarkBrown1')

# define window elements
L_F1 = [[psg.Text('Preview Image/Frame 1')],
          [psg.Input(), psg.FileBrowse()],
          [psg.OK(), psg.Cancel()]]
"""UI elements for selecting frame 1."""
L_F2 = [[psg.Frame('Hidden Image/Frame 2', [
          [psg.Input(), psg.FileBrowse()]
       ])]]
"""UI elements for selecting frame 2."""
L_GO = [[psg.OK()]]
"""UI elements for triggering generation."""
L_INFO = [[psg.StatusBar('github.com/gavboi', justification='c')]]
"""UI elements for window information."""


def main():

    layout = L_F1 + L_F2 + L_GO + L_INFO
    
    win = psg.Window('Get filename example', layout)
    event, values = win.read()
    win.close()

if __name__ == '__main__':
    main()
