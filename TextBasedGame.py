# Emily Nagorski


# The dictionary links the rooms from my map to each other.
manor_rooms = {
    'Entrance Hall': {'North': 'Study', 'South': 'Wine Cellar', 'East': 'Master Bedroom', 'West': 'Conservatory'},
    'Study': {'East': 'Ballroom', 'South': 'Entrance Hall', 'item': 'Diary'},
    'Ballroom': {'West': 'Study', 'item': 'Locket'},
    'Conservatory': {'East': 'Entrance Hall', 'item': 'Ring'},
    'Master Bedroom': {'West': 'Entrance Hall', 'item': 'Ghost Bride'},
    'Catacombs': {'East': 'Wine Cellar', 'South': 'Dungeon', 'item': 'Rusted Key'},
    'Wine Cellar': {'West': 'Catacombs', 'North': 'Entrance Hall', 'East': 'Gallery', 'item': 'Candle'},
    'Gallery': {'West': 'Wine Cellar', 'South': 'Library', 'item': 'Music Box'},
    'Dungeon': {'North': 'Catacombs', 'item': 'Ceremonial Robe'},
    'Library': {'North': 'Gallery', 'East': 'Balcony', 'item': 'Broken Vial'},
    'Balcony': {'West': 'Library', 'item': 'Dusty Mirror'}
}


def string_split(movement):  # split the user input, in order to iterate over dictionary
    move_split = movement.split()
    return move_split


def player_status(room):  # lets the player know where they are in the map
    return f'You are in the {room}'


def room_item(room_name):  # shows player what item is in their current room, if they've added it to their inventory
    item = manor_rooms[room_name].get('item', '')       # then it will be blank
    if item:
        if item not in item_inventory:
            return f'You see a {item}'
        else:
            return ''
    else:
        return ''


def move_user(room, user_input):  # moves the user though the map, returning the new room
    move = manor_rooms[room].get(user_input)
    return move


def is_valid_move(room, user_text):  # validates the user's input, to verify that it is a possible command
    if not user_text or len(user_text) == 1:  # validates that input is not empty and there is more than one word
        return False
    elif user_text[0] == 'go':
        valid_go = manor_rooms[room].get(user_text[1])
        if valid_go:
            return True
    elif user_text[0] == 'get':
        valid_get = manor_rooms[room].get('item')
        if valid_get == " ".join(user_text[1:]):
            return True
    else:
        return False


current_room = 'Entrance Hall'  # assigning room variable where all players will begin

item_inventory = []     # empty inventory, that the player will add to

# list below is a list of items the player needs in order to win
winning_inventory = ['Locket', 'Diary', 'Ring', 'Rusted Key', 'Candle', 'Music Box', 'Ceremonial Robe', 'Broken Vial']


print('Welcome to the Oakland Haunted Manor. The door creaks open, and you enter a very dusty Entrance Hall.\n'
      'Your objective is to collect the 8 items involved in the Ghost Bride’s murder and curse.\n'
      'Pick up each of these items and upon collection of all the items return to the Entrance Hall to destroy them.\n'
      'Once destroyed you will free her from the grounds.\n'
      'But beware of the Ghost Bride...\n'
      'She is not fond of visitors and disrupting her sleep will cause you to lose the game.\n'
      'Also be wary of picking up anything that would show the Bride your whereabouts through a reflection..\n'
      'This will also end the game.\n')
print('To move through the manor, type: go North, go South, go East, go West, or type exit, to leave the game.\n')
print('You can also type get Ring...and fill in whichever item is in the room with you, to add it to your inventory.\n')

playing_game = True
while playing_game:  # main game play loop, that calls functions, and exits the game if commanded, or if player loses
    win_check = all(item in item_inventory for item in winning_inventory)
    if win_check:
        exit('Congratulations, you retrieved all the items! You returned to the Entrance Hall,'
             ' and destroyed the items to break the curse of the Ghost Bride.')
    if 'Dusty Mirror' in item_inventory:
        exit('Oh No! You revealed your location to the Ghost Bride, you have angered her. Game Over.')

    if current_room == 'Master Bedroom':    # check lose condition
        exit('You have disrupted the Ghost Bride. Game Over.')

    print('------------------------------------')   # player status
    print(player_status(current_room))
    print(room_item(current_room))
    print(f'Current Inventory:{item_inventory}')

    user_move = input('Enter your move:\n')  # asking for user input

    if user_move == 'exit':  # checking to see if player wants to leave the game
        exit('Thanks for playing the game. Hope you enjoyed it.')

    input_split = string_split(user_move)

    if is_valid_move(current_room, input_split):  # calls back to function, to validate user input
        if input_split[0] == 'go':
            current_room = move_user(current_room, input_split[1])  # reassigns current_room variable to new location
        else:
            picked_item = " ".join(input_split[1:])
            item_inventory.append(picked_item)    # adds item to item inventory list
            print(f'Retrieved the {picked_item}!')
    else:
        print('Invalid entry, please try again')
