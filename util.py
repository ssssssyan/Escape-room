def printWelcomeMessage():
  print('''
Escape Room
========================
Find the exit!
Commands:
    go   <PLACE>
    get  <ITEM>
''')

def printStatus(current_place, inventory, game_map):
  print('\n--------------------')
  print('You are in', current_place)
  print('You can go to:', ', '.join(game_map[current_place]['neighbors']))
  print('You can see:', ', '.join(game_map[current_place]['items']))
  print('Inventory:', ', '.join(inventory))
  print('--------------------\n')


def readInput():
  playerInput = input('>').lower().split()
  while not len(playerInput) == 2:
    playerInput = input('>').lower().split()
  return playerInput
  
