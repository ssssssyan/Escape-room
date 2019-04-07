#!/bin/python3

# Welcome Message
print('''
Escape Room
========================
After a day of work, you are trying to leave the office!
Commands:
    go   <PLACE>
    get  <ITEM>
''')

# Office Map
office = {
    # 21F
    'mpr': {
        'adjacent_places': ['pantry']},
    'pantry': {
        'adjacent_places': ['mpr', 'front desk', '21f stairs'],
        'items': ['coffee']},
    'front desk': {
        'adjacent_places':['pantry'],
        'is_exit': True,
        'exit_items': ['badge']},
    '21f stairs': {
        'adjacent_places': ['pantry', '20f stairs']},
    # 20F
    '20f stairs': {
        'adjacent_places': ['21f stairs', 'matsuri']},
    'matsuri': {
        'adjacent_places': ['20f stairs'],
        'items': ['badge']}
}

# Player variables
inventory = []
currentPlace = 'mpr'

# Game logic
while True:

    # Show current player status
    print('--------------------')
    print(f'You are in {currentPlace}')
    print(f'Inventory: {inventory}')
    if office[currentPlace].get('items', []):
        print(f"You see {', '.join(office[currentPlace]['items'])} in here")
    print(f"You can go to: {', '.join(office[currentPlace]['adjacent_places'])}")

    # Check if player can win the game
    if office[currentPlace].get('is_exit', False):
        print(f'You can get out of the office from here!')
        if 'exit_items' in office[currentPlace]:
            print('To leave from here, you need: '
                    f"{', '.join(office[currentPlace]['exit_items'])}")
            print('Checking your invenory....')
        if all([item in inventory for item in office[currentPlace]['exit_items']]):
            print('You have all of the items required!!')
            print('Leaving office now.. OTSUKARE! YOU WIN!')
            break
        else:
            print("Looks like you don't have all items needed yet, keep going!")

    # Take player input
    move = ''
    while not move:
        move = input('>')
    move = move.lower().split(' ', 1)

    # Handle 'goto' action
    if move[0] == 'go':
        destination = move[1]
        if destination in office[currentPlace]['adjacent_places'] and \
                destination in office:
            currentPlace = destination
        else:
            print('Ooops, the place you are trying to go does not exist!')

    # Handle 'get' action
    if move[0] == 'get':
        item = move[1]
        if item in office[currentPlace].get('items', []):
            inventory.append(item)
            print(f'{item} got!')
            office[currentPlace]['items'].remove(item)
        else:
            print('Ooops, the item you are trying to get does not exist!')
    
    # Handle invalid action
    else:
        print('Invalid action.')
