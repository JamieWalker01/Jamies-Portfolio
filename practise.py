from random import randint
from random import choice

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

def random_row2():
    added_row = randint(random_row(board)-1, random_row(board)+1, 2)
    if added_row in range(0, 5):
        return added_row
    else:
        random_row2()

def random_col2():
    added_col = randint(random_col(board)-1, random_col(board)+1, 2)
    if added_col in range(0, 5):
        return added_col
    else:
        random_col2()

ship_row = random_row(board)
ship_col = random_col(board)

def ship_tail():
    rand_ele = choice([random_row2, random_col2])
    if rand_ele == random_row2:
        return [rand_ele][ship_col]
    else:
        return [rand_ele][ship_row]


def play_game():
  for turn in range(10):
    print ("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if board[ship_row][ship_col] == 'X' and board(ship_tail()) == 'X':
      print ("Congratulations! You sank my battleship!")
      break    
    else:
      if guess_row not in range(5) or \
      guess_col not in range(5):
        print ("Oops, that's not even in the ocean.")
      elif board[guess_row][guess_col] == "X":
        print( "You guessed that one already." )
      else:
        print ("You missed my battleship!")
        board[guess_row][guess_col] = "X"
      print_board(board)
    if turn == 9:
      print ('Game Over')
      rematch = input('Do you want a rematch?: ')
      if rematch == 'yes':
        play_game()
      elif rematch == 'no':
        print ('OK, see ya!')