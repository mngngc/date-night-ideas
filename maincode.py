import sys
import PySimpleGUI as sg
import csv
import random
import webbrowser

sg.theme('DarkTeal2')

# defines main welcome screen
def welcome():
    layout = [
        [sg.Text("Welcome to Let's Go Out!", font=("Arial", 25))],
        [sg.Text('The best way to find a date night idea!', font=("Arial", 15))],
        [sg.Button('Click me to begin!', expand_x=True, expand_y=True, font=("Arial", 15))]
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
        [sg.Text("Hello! What are you looking to do this evening?", font=("Arial", 15))],
        [sg.Button("Get Food!", expand_x=True, expand_y=True, font=("Arial", 15)), sg.Button("Have a Drink!", expand_x=True, expand_y=True, font=("Arial", 15))],
        [sg.Button("Go On An Adventure!", expand_x=True, expand_y=True, font=("Arial", 15)), sg.Button("Surprise Me!", expand_x=True, expand_y=True, font=("Arial", 15))]
    ]

    # create the window
    window = sg.Window("Let's Go Out", layout, size=(500,250), element_justification='c')

    while True:
        event, values = window.read()
        # End program if user closes window or
        # move different response function 
        if event == sg.WIN_CLOSED:
             break
        elif event == "Get Food!":
            window.close()
            dinner()
        elif event == "Have a Drink!":
            window.close()
            drinks()
        elif event == "Go On An Adventure!":
            window.close()
            adventure()
        elif event == "Surprise Me!":
            window.close()
            surprise()
            
    window.close()

# defines response dinner
def dinner():
    with open("restaurants.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for index, row in enumerate(csv_reader):
            if index == 0:
                chosen_row = row
            else:
                r = random.randint(0, index)
                if r == 0:
                    chosen_row = row
        result_string = "I have selected {name}!\nThey are located at, {address}\nThey can be reached at, {number}\nLook to spend {cost}\nWebsite: {web}"
        result_string = result_string.format(name=chosen_row[0], number=chosen_row[1], cost=chosen_row[2], address=chosen_row[3], web=chosen_row[4])
        site = chosen_row[4]

    def callback(url):
        webbrowser.open_new(site)


    layout = [
        [sg.Text("Dinner!", font=("Arial", 25))],
        [sg.Text(result_string, font=("Arial", 10))],
        [sg.Text(site, font=("Arial", 10), tooltip=site, enable_events=True)]
    ]

    # create the window
    window = sg.Window("Let's Go Out", layout, size=(500,250), element_justification='c')

    while True:
        event, values = window.read()
        # End program if user closes window or
        if event == sg.WIN_CLOSED:
            break
    window.close()

# defines response movie
def drinks():
    with open("bars.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for index, row in enumerate(csv_reader):
            if index == 0:
                chosen_row = row
            else:
                r = random.randint(0, index)
                if r == 0:
                    chosen_row = row
        result_string = "I have selected {name}!\nThey can be reached at, {number}\nLook to spend {cost}"
        result_string = result_string.format(name=chosen_row[0], number=chosen_row[1], cost=chosen_row[2])
        
    layout = [
        [sg.Text("Drinks!", font=("Arial", 25))],
        [sg.Text(result_string, font=("Arial", 10))]
    ]

    # create the window
    window = sg.Window("Let's Go Out", layout, size=(500,250), element_justification='c')

    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses OK
        if event == sg.WIN_CLOSED:
            break
    window.close()

# defines response adventure
def adventure():
    with open("adventures.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for index, row in enumerate(csv_reader):
            if index == 0:
                chosen_row = row
            else:
                r = random.randint(0, index)
                if r == 0:
                    chosen_row = row
        result_string = "I have selected {name}!\nThey can be reached at, {number}\nLook to spend {cost}"
        result_string = result_string.format(name=chosen_row[0], number=chosen_row[1], cost=chosen_row[2])

    layout = [
        [sg.Text("Adventure!", font=("Arial", 25))],
        [sg.Text(result_string, font=("Arial", 10))]
    ]

    # create the window
    window = sg.Window("Let's Go Out", layout, size=(500,250), element_justification='c')

    while True:
        event, values = window.read()
        # End program if user closes window
        if event == sg.WIN_CLOSED:
            break
    window.close()


# defines response surprise me
def surprise():
    with open("surprise.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for index, row in enumerate(csv_reader):
            if index == 0:
                chosen_row = row
            else:
                r = random.randint(0, index)
                if r == 0:
                    chosen_row = row
        result_string = "I have selected {name}!\nThey are located at, {address}\nThey can be reached at, {number}\nLook to spend {cost}\nWebsite: {web}"
        result_string = result_string.format(name=chosen_row[0], number=chosen_row[1], cost=chosen_row[2], address=chosen_row[3], web=chosen_row[4])

    layout = [
        [sg.Text("Surprise!", font=("Arial", 25))],
        [sg.Text(result_string, font=("Arial", 10))]
    ]

    # create the window
    window = sg.Window("Let's Go Out", layout, size=(500,250), element_justification='c')

    while True:
        event, values = window.read()
        # End program if user closes window or
        if event == sg.WIN_CLOSED:
            break
    window.close()


if __name__ == '__main__':
    welcome()