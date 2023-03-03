"""This module creates a window that allows users to select parameters more
easily. NOT YET FUNCTIONAL

Contains:

    * :func:`main`
"""

print("Not working yet!")
input("(Press enter)")
exit()

import PySimpleGUI as sg

sg.theme('Dark Grey 13')

layout = [[sg.Text('Filename')],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()]]

window = sg.Window('Get filename example', layout)

event, values = window.read()
window.close()
