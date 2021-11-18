import sys
import PySimpleGUI as sg

# defines main welcome screen
def welcome():
    layout = [
        [sg.Text("Welcome to Let's Go Out!")],
        [sg.Text('The best way to find a date night idea!')],
        [sg.Button('Click me to begin!')]
    ]

    # create the window
    window = sg.Window("Let's Go Out!", layout, size=(500,250), element_justification='c')

    #create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # move to main to begin 
        if event ==sg.WIN_CLOSED:
            break
        elif event == 'Click me to begin!':
            window.close()
            main()
    window.close()

# defines main code
def main():
    layout = [
        [sg.Text("Sample Text")],
        [sg.Button("Response 1"), sg.Button("Response 2")],
        [sg.Button("Response 3"), sg.Button("Response 4")]
    ]

    # create the window
    window = sg.Window("Let's Go Out", layout, size=(500,250), element_justification='c')

    while True:
        event, values = window.read()
        # End program if user closes window or
        # move different response function 
        if event == sg.WIN_CLOSED:
             break
        elif event == "Response 1":
            window.close()
            function1()
            
    window.close()

# defines response function 1
def function1():
    layout = [
        [sg.Text("Sample return")],
        [sg.Button("OK")]
    ]

    # create the window
    window = sg.Window("Let's Go Out", layout, size=(500,250), element_justification='c')

    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses OK
        if event == "OK" or sg.WIN_CLOSED:
            break
    window.close()

if __name__ == '__main__':
    welcome()