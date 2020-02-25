#!/bin/python3
from util import printWelcomeMessage, printStatus, readInput

# Section 1: Game Map
game_map = {
  # 21F
  'mpr': {
    'neighbors': {'pantry'},
    'items': {'badge'}
  },
  'pantry': {
    'neighbors': {'mpr', 'frontdesk'},
    'items': {'coffee'}
  },
  'frontdesk': {
    'neighbors': {'pantry', 'exit'},
    'items': set()
  },
  'exit':  {
    'neighbors': {'frontdesk'},
    'items': set()
  }
}

exit_items = {'badge', 'coffee'}

# Section 2: Player variables
current_place = 'mpr'
inventory = set()
escaped = False

# Section 3: Welcome Message
printWelcomeMessage()

# Section 4: Game logic
while not escaped:
  # Section 4.1: Display current status
  printStatus(current_place, inventory, game_map)
  # Section 4.2: Read in player input
  action, option = readInput()

  # Section 4.3: Handle 'go' action
  if action == 'go':
    neighbors = game_map[current_place]['neighbors']
    if option in neighbors:
      if option in game_map:
        current_place = option
      else:
        print('Destination does not exist in map!')
    else:
      print('Destination is not next to current place!')
  
  # Section 4.4: Handle 'get' action
  elif action == 'get':
    items = game_map[current_place]['items']
    if option in items:
      inventory.add(option)
      items.remove(option)
    else:
      print('There is no', option, 'here!')
  
  # Section 4.5: Handle invalid action
  else:
    print('Invalid action.')
    
  # Section 4.6: Winning
  if current_place == 'exit':
    print('Hooray! You escaped!')
    escaped = True
