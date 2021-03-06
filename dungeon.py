import random
import os


CELLS = [ (0,0), (1,0), (2,0), (3,0), (4,0),
          (0,1), (1,1), (2,1), (3,1), (4,1),
          (0,2), (1,2), (2,2), (3,2), (4,2),
          (0,3), (1,3), (2,3), (3,3), (4,3),
          (0,4), (1,4), (2,4), (3,4), (4,4),
]

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

# get locations for player, monster, and door
def get_locations():
  return random.sample(CELLS, 3)

# move players coordinates
def move_player(player, move):
  x, y = player
  if move == "LEFT":
    x -= 1
  if move == "RIGHT":
    x += 1
  if move == "UP":
    y -= 1
  if move == "DOWN":
    y += 1
  return x, y

# get available moves per player, given the walls adjacent to them
def get_moves(player):
  moves = ["LEFT", "RIGHT", "UP", "DOWN"]
  x, y = player
  if x ==  0:
    moves.remove("LEFT")
  if x ==  4:
    moves.remove("RIGHT")
  if y ==  0:
    moves.remove("UP")
  if y ==  4:
    moves.remove("DOWN")
  return moves

# draw grid of cells with players location
def draw_map(player):
  print(" _"*5)
  tile = "|{}"

  for cell in CELLS:
    x, y = cell
    if x < 4:
      line_end = ""
      if cell == player:
        output = tile.format("X")
      else:
        output = tile.format("_")
    else:
      line_end = "\n"
      if cell == player:
        output = tile.format("X|")
      else:
        output = tile.format("_|")
    print(output, end=line_end)

# call to start the game
def game_loop():
  monster, door, player = get_locations()
  playing = True

  while playing:
      clear_screen()
      draw_map(player)
      valid_moves = get_moves(player)

      print("You are currently in room {}".format(player)) 
      print("You can move {}".format(", ".join(valid_moves))) 
      print("Enter QUIT to quit")
      
      action = input("> ").upper()
      
      if action == "QUIT":
        print("See you next time!")
        break

      if action in valid_moves:
        player = move_player(player, action)

        if player == monster:
          print("Oh no, the monster got you!")
          playing = False
        if player == door:
          print("Congrats you escaped!")
          playing = False
      else:
        input("Can't go this way, wall")

  else:
    if input("Play again? [Y/N] ").lower() != "n":
      game_loop()

clear_screen()
print("Find the door before the monster gets you.")
game_loop()
    

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  