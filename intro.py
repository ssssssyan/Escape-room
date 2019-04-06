#!/bin/python3

# Welcome Message
print('''
Escape Room
===========
Commands:
    goto <PLACE>
    get  <ITEM>
''')

# Office Map
office = {
    # 21F
    'mpr': {'adjacent_rooms': ['pantry']},
    'pantry': {'adjacent_rooms': ['mpr'], 'items':['coffee']}
}

# Player variables
inventory = []
currentRoom = 'mpr'

# Game logic
while True:
    # Show current player status
    print('--------------------')
    print(f'You are in {currentRoom}')
    print(f'Inventory: {inventory}')
    if 'items' in office[currentRoom]:
        print(f"You see {','.join(office[currentRoom]['items'])} in here")
    print(f"You can go to: {','.join(office[currentRoom]['adjacent_rooms'])}")
    
    # Take player input
    move = ''
    while not move:
        move = input('>')
    move = move.lower().split()
    
    # Handle 'goto' action
    if move[0] == 'goto':
        destination = move[1]
        if destination in office[currentRoom]['adjacent_rooms'] and \
                destination in office:
            currentRoom = destination
        else:
            print('Ooops, the place you are trying to go does not exist!')

    # Handle 'get' action
    if move[0] == 'get':
        item = move[1]
        if item in office[currentRoom].get('items', []):
            inventory.append(item)
            print(f'{item} got!')
            office[currentRoom]['items'].remove(item)
        else:
            print('Ooops, the item you are trying to get does not exist!')


