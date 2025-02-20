# Matthew Pantel
# IT-140 
# Week 7 Final Project

import sys
from time import sleep

# Global Variables 
inventory = []
current_room = 'Living Room'
villain_room = 'Ritual Chamber'
valid_rooms = {
    'Living Room': {
        'West': 'Study', 
        'East': 'Library', 
        'Downstairs': 'Storage Room', 
        'Quit': 'Quit',
        'Item': 'Flashlight'
        },
    'Study': {
        'East': 'Living Room',
        'Quit': 'Quit',
        'Item': 'Old Journal'
        },
    'Library': {
        'West': 'Living Room',
        'Upstairs': 'Master Bedroom',
        'Quit': 'Quit',
        'Item': 'Ancient Mirror'
        },
    'Master Bedroom': {
        'Downstairs': 'Library',
        'East': 'Conservatory',
        'Quit': 'Quit',
        'Item': 'Candles'
    },
    'Conservatory': {
        'West': 'Master Bedroom',
        'Quit': 'Quit',
        'Item': 'Magic Crystals'
    },
    'Storage Room':{
        'West': 'Ritual Chamber', 
        'East': 'Wine Cellar',
        'Upstairs': 'Living Room',
        'Quit': 'Quit',
        'Item': 'Matches'
    },
    'Wine Cellar': {
        'West': 'Storage Room',
        'Quit': 'Quit',
        'Item': 'Chalk'
    },
    'Ritual Chamber': {
        'East': 'Storage Room',
        'Quit': 'Quit'
    }
}

def menu():
    print('''
        \r***** Intro To Scripting *****
        \n[Start] Start the Game
        \r[Help] Help Menu
        \r[Quit] Quit the game''')       
        
    choice = input('\nWhat do you want to do: ').strip().lower()
    if choice == 'start':
        print('You clicked start')
    elif choice == 'help':
        print('You clicked help')
    elif choice == 'quit':
        print('Exiting the game...')
        sys.exit()
    else:
        input('''****** ERROR ******
            \nPlease choose only the options above.
            \nPress ENTER to try again.''')
        



def main():
    pass


def living_room():
    global inventory
    global current_room
    item = valid_rooms['Living Room']['Item']
    print(item)
    


def study():
    pass


def library():
    pass


def master_bedroom():
    pass


def conservatory():
    pass


def storage_room():
    pass


def wine_cellar():
    pass


def ritual_chamber():
    pass


if __name__ == "__main__":
    menu()