# Matthew Pantel
# IT-140 
# Week 7 Final Project

import sys
from time import sleep

# Global Variables 
inventory = []
current_room = 'Living Room'
villain_room = 'Ritual Chamber'
valid_items = ['Flashlight', 'Old Journal', 'Ancient Mirror', 'Candles', 'Magic Crystals', 'Matches', 'Chalk']
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

# Here is the main menu function. This will not only start the game, but quit the game as well. I use the sleep() method to counter the immediate printing of statments after a user provides a choice. 

def menu():
    print('''
        \r***** Intro To Scripting *****
        \n[Start] Start the Game
        \r[Help] Help Menu
        \r[Quit] Quit the game''')
    
    while True:
        choice = input('\nWhat do you want to do: ').strip().lower()
        if choice == 'start':
            print('Starting game...')
            sleep(1)
            living_room()
            break
        elif choice == 'help':
            print('''
                \nYou receive a mysterious package with no return address. Inside is a note with cryptic instructions:
                  \nGather the [7 Items] from the mansion,
                  \rComplete the [Ritual] in the Chambers,
                  \rBeat the Shadowy [Villain]
                  \nThe note also includes a rough map of a large estate with various rooms marked with one of the room labeled with a warning.\r
                  ''')
        elif choice == 'quit':
            print('Exiting the game...')
            sleep(1)
            sys.exit()
        else:
            input('''****** ERROR ******
                \nPlease choose only the options above.
                \nPress ENTER to try again.''')

# Functions for each room that handles the users input and validates the input. 
# If the input is invalid, it'll throw a readable error

def living_room():
    global inventory
    global current_room
    current_room = 'Living Room'
    item = valid_rooms['Living Room']['Item']
    print('''
        \nMoonlight filters through dusty windows, casting long shadows across Victorian furniture. \nA [flashlight] catches your eye, its metal surface gleaming on an antique side table.
          \n[Item] Pick up the item
          \r[Inventory] Check your inventory
          \r[West] Move to the Study
          \r[East] Move to the Library
          \r[Downstairs] Move to the Storage Room
          \r[Quit] Quit the game
        ''')
    while True:
        choice = input('What do you want to do: ').strip().lower()
        if choice == 'item':
            if item not in inventory:
                inventory.append(item)
                print(f'You have picked up the {item}.')
            else:
                print('You have already picked up this item.')
        elif choice == 'inventory':
            if len(inventory) == 0:
                print('Your inventory is empty.')
            else:
                print('Your inventory contains: ')
                for item in inventory:
                    print(f'- {item}')
        elif choice == 'west':
            study()
            break
        elif choice == 'east':
            library()
            break
        elif choice == 'downstairs':
            storage_room()
            break
        elif choice == 'quit':
            print('Exiting the game...')
            sleep(1)
            sys.exit()
        else:
            input('''****** ERROR ******
                \nPlease choose only the options above.
                \nPress ENTER to try again.''')

def study():
    global inventory
    global current_room
    current_room = 'Study'
    item = valid_rooms['Study']['Item']
    print('''
        \nThe Study is filled with the scent of old books and parchment. \nA sense of foreboding hangs in the air, and you spot a [Old Journal] glinting on the desk under the dim light.
          \n[Item] Pick up the item
          \r[Inventory] Check your inventory
          \r[East] Move to the Living Room
          \r[Quit] Quit the game
        ''')
    while True:
        choice = input('What do you want to do: ').strip().lower()
        if choice == 'item':
            if item not in inventory:
                inventory.append(item)
                print(f'\nYou have picked up the {item}.')
            else:
                print('\nYou have already picked up this item.')
        elif choice == 'inventory':
            if len(inventory) == 0:
                print('Your inventory is empty.')
            else:
                print('Your inventory contains: ')
                for item in inventory:
                    print(f'- {item}')
        elif choice == 'east':
            living_room()
            break
        elif choice == 'quit':
            print('Exiting the game...')
            sleep(1)
            sys.exit()
        else:
            input('''****** ERROR ******
                \nPlease choose only the options above.
                \nPress ENTER to try again.''')

def library():
    global inventory
    global current_room
    current_room = 'Library'
    item = valid_rooms['Library']['Item']
    print('''
        \nThe Library is a labyrinth of towering bookshelves, filled with ancient tomes and forgotten knowledge. \nAmidst the dust and cobwebs, you notice an [Ancient Mirror] tucked between two books.
          \n[Item] Pick up the item
          \r[Inventory] Check your inventory
          \r[West] Move to the Living Room
          \r[Upstairs] Move to the Master Bedroom
          \r[Quit] Quit the game
        ''')
    while True:
        choice = input('What do you want to do: ').strip().lower()
        if choice == 'item':
            if item not in inventory:
                inventory.append(item)
                print(f'You have picked up the {item}.')
            else:
                print('You have already picked up this item.')
        elif choice == 'inventory':
            if len(inventory) == 0:
                print('Your inventory is empty.')
            else:
                print('Your inventory contains: ')
                for item in inventory:
                    print(f'- {item}')
        elif choice == 'west':
            living_room()
            break
        elif choice == 'upstairs':
            master_bedroom()
            break
        elif choice == 'quit':
            print('Exiting the game...')
            sleep(1)
            sys.exit()
        else:
            input('''****** ERROR ******
                \nPlease choose only the options above.
                \nPress ENTER to try again.''')

def master_bedroom():
    global inventory
    global current_room
    current_room = 'Master Bedroom'
    item = valid_rooms['Master Bedroom']['Item']
    print('''
        \nThe Master Bedroom is filled with an unsettling calm. \nOn the nightstand, you see a set of [Candles] that seem to flicker with an unnatural light.
          \n[Item] Pick up the item
          \r[Inventory] Check your inventory
          \r[Downstairs] Move to the Library
          \r[East] Move to the Conservatory
          \r[Quit] Quit the game
        ''')
    while True:
        choice = input('What do you want to do: ').strip().lower()
        if choice == 'item':
            if item not in inventory:
                inventory.append(item)
                print(f'You have picked up the {item}.')
            else:
                print('You have already picked up this item.')
        elif choice == 'inventory':
            if len(inventory) == 0:
                print('Your inventory is empty.')
            else:
                print('Your inventory contains: ')
                for item in inventory:
                    print(f'- {item}')
        elif choice == 'downstairs':
            library()
            break
        elif choice == 'east':
            conservatory()
            break
        elif choice == 'quit':
            print('Exiting the game...')
            sleep(1)
            sys.exit()
        else:
            input('''****** ERROR ******
                \nPlease choose only the options above.
                \nPress ENTER to try again.''')

def conservatory():
    global inventory
    global current_room
    current_room = 'Conservatory'
    item = valid_rooms['Conservatory']['Item']
    print('''
        \nThe Conservatory is filled with exotic plants and a strange, otherworldly glow. \nIn the center, you find a cluster of [Magic Crystals] that pulse with a faint light.
          \n[Item] Pick up the item
          \r[Inventory] Check your inventory
          \r[West] Move to the Master Bedroom
          \r[Quit] Quit the game
        ''')
    while True:
        choice = input('What do you want to do: ').strip().lower()
        if choice == 'item':
            if item not in inventory:
                inventory.append(item)
                print(f'You have picked up the {item}.')
            else:
                print('You have already picked up this item.')
        elif choice == 'inventory':
            if len(inventory) == 0:
                print('Your inventory is empty.')
            else:
                print('Your inventory contains: ')
                for item in inventory:
                    print(f'- {item}')
        elif choice == 'west':
            master_bedroom()
            break
        elif choice == 'quit':
            print('Exiting the game...')
            sleep(1)
            sys.exit()
        else:
            input('''****** ERROR ******
                \nPlease choose only the options above.
                \nPress ENTER to try again.''')

def storage_room():
    global inventory
    global current_room
    current_room = 'Storage Room'
    item = valid_rooms['Storage Room']['Item']
    print('''
        \nThe Storage Room is cluttered with old furniture and forgotten relics. \nAmong the debris, you find a box of [Matches] that might prove useful.
          \n[Item] Pick up the item
          \r[Inventory] Check your inventory
          \r[West] Move to the Ritual Chamber
          \r[East] Move to the Wine Cellar
          \r[Upstairs] Move to the Living Room
          \r[Quit] Quit the game
        ''')
    while True:
        choice = input('What do you want to do: ').strip().lower()
        if choice == 'item':
            if item not in inventory:
                inventory.append(item)
                print(f'You have picked up the {item}.')
            else:
                print('You have already picked up this item.')
        elif choice == 'inventory':
            if len(inventory) == 0:
                print('Your inventory is empty.')
            else:
                print('Your inventory contains: ')
                for item in inventory:
                    print(f'- {item}')
        elif choice == 'west':
            ritual_chamber()
            break
        elif choice == 'east':
            wine_cellar()
            break
        elif choice == 'upstairs':
            living_room()
            break
        elif choice == 'quit':
            print('Exiting the game...')
            sleep(1)
            sys.exit()
        else:
            input('''****** ERROR ******
                \nPlease choose only the options above.
                \nPress ENTER to try again.''')

def wine_cellar():
    global inventory
    global current_room
    current_room = 'Wine Cellar'
    item = valid_rooms['Wine Cellar']['Item']
    print('''
        \nThe Wine Cellar is cold and damp, with the smell of aged wine filling the air. \nOn a dusty shelf, you find a piece of [Chalk] that might be useful for the ritual.
          \n[Item] Pick up the item
          \r[Inventory] Check your inventory
          \r[West] Move to the Storage Room
          \r[Quit] Quit the game
        ''')
    while True:
        choice = input('What do you want to do: ').strip().lower()
        if choice == 'item':
            if item not in inventory:
                inventory.append(item)
                print(f'You have picked up the {item}.')
            else:
                print('You have already picked up this item.')
        elif choice == 'inventory':
            if len(inventory) == 0:
                print('Your inventory is empty.')
            else:
                print('Your inventory contains: ')
                for item in inventory:
                    print(f'- {item}')
        elif choice == 'west':
            storage_room()
            break
        elif choice == 'quit':
            print('Exiting the game...')
            sleep(1)
            sys.exit()
        else:
            input('''****** ERROR ******
                \nPlease choose only the options above.
                \nPress ENTER to try again.''')

# The Ritual Chamber is the End Game room. This is where the game will validate the user's inventory for all 7 items. If the user has all 7, then they win...if not, they'll lose the game and the game will exit. 

def ritual_chamber():
    global inventory
    global current_room
    current_room = 'Ritual Chamber'
    print('''
        \nYou have entered the Ritual Chamber. The air is thick with tension, and you can feel the presence of a dark force.\nYou check your [Inventory] to see if you have all the items to perform the ritual.
          \r[Inventory] Check your inventory
          \r[Quit] Quit the game
        ''')
    while True:
        choice = input('What do you want to do: ').strip().lower()
        if choice == 'inventory':
            if len(inventory) == 0:
                print('Your inventory is empty.')
            else:
                print('Your inventory contains: ')
                for item in inventory:
                    print(f'- {item}')
            if set(valid_items).issubset(set(inventory)):
                print('You have all the necessary items to complete the ritual and banish the darkness. You win!')
                sys.exit()
            else:
                print('You do not have all the necessary items. The darkness consumes you and you lose!')
                sys.exit()
        elif choice == 'quit':
            print('Exiting the game...')
            sleep(1)
            sys.exit()
        else:
            input('''****** ERROR ******
                \nPlease choose only the options above.
                \nPress ENTER to try again.''')

# The dunder main statement is here, since we are running this file directly, it'll tell the compiler which function to run first. If we add this file to a larger project, and run the app.js or another "starter" file, then this statement would be ignored.
if __name__ == "__main__":
    menu()