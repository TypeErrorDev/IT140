# Matthew Pantel
# IT-140 Final Assignment

# Code Style Guide: https://peps.python.org/pep-0008/

import sys

# global variables
inventory = []
current_room = 'Living Room'
valid_items = ['Flashlight', 'Old Journal', 'Ancient Mirror', 'Candles', 'Magic Crystals', 'Matches', 'Chalk']
villain_room = 'Ritual Chamber'

# Set the dictionary for the rooms and valid moves
valid_moves = {
    "Living Room": {"W": "Study", "E": "Library", "D": "Storage Room", "Q": "Quit"},
    "Study": {"E": "Living Room", "Q": "Quit"}, 
    "Library": {"W": "Living Room", "U": "Master Bedroom", "Q": "Quit"}, 
    "Master Bedroom": {"D": "Library", "E": "Conservatory", "Q": "Quit"}, 
    "Conservatory": {"W": "Master Bedroom", "Q": "Quit"}, 
    "Storage Room": {"U": "Living Room", "W": "Ritual Chamber", "E": "Wine Cellar", "Q": "Quit"}, 
    "Ritual Chamber": {"E": "Storage Room", "Q": "Quit"}, 
    "Wine Cellar": {"W": "Storage Room", "Q": "Quit"} 
}

# Room descriptions and items
room_descriptions = {
    "Living Room": "As you step into the Living Room, the air feels heavy with an eerie silence.\nShadows dance across the walls, and you notice a [Flashlight] lying on an old, dusty table.",
    "Study": "The Study is filled with the scent of old books and parchment.\nA sense of foreboding hangs in the air, and you spot a [Old Journal] glinting on the desk under the dim light.",
    "Library": "The Library is a labyrinth of towering bookshelves, filled with ancient tomes and forgotten knowledge.\nAmidst the dust and cobwebs, you notice an [Ancient Mirror] tucked between two books.",
    "Master Bedroom": "The Master Bedroom is filled with an unsettling calm.\nOn the nightstand, you see a set of [Candles] that seem to flicker with an unnatural light.",
    "Conservatory": "The Conservatory is filled with exotic plants and a strange, otherworldly glow.\nIn the center, you find a cluster of [Magic Crystals] that pulse with a faint light.",
    "Storage Room": "The Storage Room is cluttered with old furniture and forgotten relics.\nAmong the debris, you find a box of [Matches] that might prove useful.",
    "Ritual Chamber": "You have entered the Ritual Chamber. The air is thick with tension, and you can feel the presence of a dark force.",
    "Wine Cellar": "The Wine Cellar is cold and damp, with the smell of aged wine filling the air.\nOn a dusty shelf, you find a piece of [Chalk] that might be useful for the ritual."
}

room_items = {
    "Living Room": "Flashlight",
    "Study": "Old Journal",
    "Library": "Ancient Mirror",
    "Master Bedroom": "Candles",
    "Conservatory": "Magic Crystals",
    "Storage Room": "Matches",
    "Wine Cellar": "Chalk"
}

def move_rooms(current_room, direction):
    if direction in valid_moves[current_room]:
        new_room = valid_moves[current_room][direction]
        if new_room == "Quit":
            print('Exiting the game...')
            sys.exit()
        return new_room
    else:
        print("You are looking at the wall. Please turn around and try another way!")
        return current_room

def show_status(current_room):
    print(room_descriptions[current_room])
    if current_room in room_items and room_items[current_room] not in inventory:
        print(f"\n[Item] Pick up the {room_items[current_room]}")
    print("\r[Inventory] Check Your Inventory")
    for direction in valid_moves[current_room]:
        if direction == "Q":
            print("\r[Q] Quit")
        else:
            print(f"\r[{direction}] Move {direction}")

def get_user_choice():
    while True:
        choice = input('\nWhat would you like to do? ').lower().strip()
        if choice in ['inventory', 'inv', 'enter', 'q', 'item'] or choice in ['w', 'e', 'd', 'u']:
            return choice
        else:
            input('''****** ERROR ******
                \nPlease choose only the options above.
                \nPress ENTER to try again.''')

def living_room():
    global current_room
    current_room = 'Living Room'
    while current_room == 'Living Room':
        show_status(current_room)
        choice = get_user_choice()
        if choice == 'item' and room_items[current_room] not in inventory:
            inventory.append(room_items[current_room])
            print(f'You have picked up the {room_items[current_room]} and placed it in your bag!')
        elif choice in ['inventory', 'inv']:
            if len(inventory) == 0:
                print('Your inventory is empty.')
            else:
                print('Your inventory contains: ')
                for item in inventory:
                    print(f'- {item}')
        else:
            current_room = move_rooms(current_room, choice.upper())

def study():
    global current_room
    current_room = 'Study'
    while current_room == 'Study':
        show_status(current_room)
        choice = get_user_choice()
        if choice == 'item' and room_items[current_room] not in inventory:
            inventory.append(room_items[current_room])
            print(f'You have picked up the {room_items[current_room]} and placed it in your bag!')
        elif choice in ['inventory', 'inv']:
            if len(inventory) == 0:
                print('Your inventory is empty.')
            else:
                print('Your inventory contains: ')
                for item in inventory:
                    print(f'- {item}')
        else:
            current_room = move_rooms(current_room, choice.upper())

def library():
    global current_room
    current_room = 'Library'
    while current_room == 'Library':
        show_status(current_room)
        choice = get_user_choice()
        if choice == 'item' and room_items[current_room] not in inventory:
            inventory.append(room_items[current_room])
            print(f'You have picked up the {room_items[current_room]} and placed it in your bag!')
        elif choice in ['inventory', 'inv']:
            if len(inventory) == 0:
                print('Your inventory is empty.')
            else:
                print('Your inventory contains: ')
                for item in inventory:
                    print(f'- {item}')
        else:
            current_room = move_rooms(current_room, choice.upper())

def master_bedroom():
    global current_room
    current_room = 'Master Bedroom'
    while current_room == 'Master Bedroom':
        show_status(current_room)
        choice = get_user_choice()
        if choice == 'item' and room_items[current_room] not in inventory:
            inventory.append(room_items[current_room])
            print(f'You have picked up the {room_items[current_room]} and placed it in your bag!')
        elif choice in ['inventory', 'inv']:
            if len(inventory) == 0:
                print('Your inventory is empty.')
            else:
                print('Your inventory contains: ')
                for item in inventory:
                    print(f'- {item}')
        else:
            current_room = move_rooms(current_room, choice.upper())

def conservatory():
    global current_room
    current_room = 'Conservatory'
    while current_room == 'Conservatory':
        show_status(current_room)
        choice = get_user_choice()
        if choice == 'item' and room_items[current_room] not in inventory:
            inventory.append(room_items[current_room])
            print(f'You have picked up the {room_items[current_room]} and placed it in your bag!')
        elif choice in ['inventory', 'inv']:
            if len(inventory) == 0:
                print('Your inventory is empty.')
            else:
                print('Your inventory contains: ')
                for item in inventory:
                    print(f'- {item}')
        else:
            current_room = move_rooms(current_room, choice.upper())

def storage_room():
    global current_room
    current_room = 'Storage Room'
    while current_room == 'Storage Room':
        show_status(current_room)
        choice = get_user_choice()
        if choice == 'item' and room_items[current_room] not in inventory:
            inventory.append(room_items[current_room])
            print(f'You have picked up the {room_items[current_room]} and placed it in your bag!')
        elif choice in ['inventory', 'inv']:
            if len(inventory) == 0:
                print('Your inventory is empty.')
            else:
                print('Your inventory contains: ')
                for item in inventory:
                    print(f'- {item}')
        else:
            current_room = move_rooms(current_room, choice.upper())

def ritual_chamber():
    global current_room
    current_room = 'Ritual Chamber'
    while current_room == 'Ritual Chamber':
        show_status(current_room)
        choice = get_user_choice()
        if choice == 'item' and room_items[current_room] not in inventory:
            inventory.append(room_items[current_room])
            print(f'You have picked up the {room_items[current_room]} and placed it in your bag!')
        elif choice in ['inventory', 'inv']:
            if len(inventory) == 0:
                print('Your inventory is empty.')
            else:
                print('Your inventory contains: ')
                for item in inventory:
                    print(f'- {item}')
        else:
            current_room = move_rooms(current_room, choice.upper())
            if current_room == villain_room:
                if set(valid_items).issubset(set(inventory)):
                    print('You have all the necessary items to complete the ritual and banish the darkness. You win!')
                else:
                    print('You do not have all the necessary items. The darkness consumes you and you lose!')
                sys.exit()

def menu():
    print('''
            \nAs you approach the Mansion, you feel a shiver roll down your\nspine and the hairs on your neck start to stand.\nYou place your foot on the first step and you hear a loud,\near ripping creak and the door slowly opens a bit.
            \n[Inventory] Check Your Inventory
            \r[Help] View the Help Menu
            \r[Enter] Enter the Mansion
            \r[Q] Quit
            ''')
    
    choice = get_user_choice()
    if choice == 'inventory' or choice == 'inv':
        if len(inventory) == 0:
            print('Your inventory is empty.')
        else:
            print('Your inventory contains: ')
            for item in inventory:
                print(f'- {item}')
    elif choice == 'help':
        print('''
            You receive a mysterious package with no return address. Inside is a note with cryptic instructions: “Enter the mansion. Collect the items. Avoid the shadow.” The note also includes a rough map of a large estate with various rooms marked. No further explanation is provided, but the handwriting is eerily familiar.

            Curiosity compels you to investigate. Upon arriving at the mansion, you find the doors unlocked and the air thick with tension. As you explore, it becomes clear that the mansion holds more than just secrets—it’s filled with strange, useful items scattered across its rooms. However, there’s something else lurking in the shadows, an unseen presence that grows stronger the longer you stay.
            ''')
    elif choice == 'enter':
        main()
    elif choice == 'q':
        print('Exiting the game...')
        sys.exit()

def main():
    global current_room
    while True:
        if current_room == 'Living Room':
            living_room()
        elif current_room == 'Study':
            study()
        elif current_room == 'Library':
            library()
        elif current_room == 'Master Bedroom':
            master_bedroom()
        elif current_room == 'Conservatory':
            conservatory()
        elif current_room == 'Storage Room':
            storage_room()
        elif current_room == 'Ritual Chamber':
            ritual_chamber()

if __name__ == "__main__":
    menu()