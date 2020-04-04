from random import randint
from random import choice

board = []

for x in range(0, 6):
  board.append(["O"] * 6)

board[0][1:6] = ['1', '2', '3', '4', '5']
board[1:6][0] = ['1', '2', '3', '4', '5']

def print_board(board):
  for row in board:
    print (" ".join(row))

def random_row(board):
  return randint(1, len(board) - 1)

def random_col(board):
  return randint(1, len(board[0]) - 1)

def random_row2():
    added_row = choice([random_row(board)-1, random_row(board)+1])
    if added_row in range(1, 6):
        return added_row
    else:
        random_row2()

def random_col2():
    added_col = choice([random_col(board)-1, random_col(board)+1])
    if added_col in range(1, 6):
        return added_col
    else:
        random_col2()

ship_row = random_row(board)
ship_col = random_col(board)

def ship_tail():
    new_cord = choice([random_row2, random_col2])
    if new_cord == random_row2:
        ship_row2 = new_cord
        ship_col2 = ship_col
    elif new_cord == random_col2():
        ship_row2 = ship_row
        ship_col2 = new_cord 

ship_tail()


def play_game():
  for turn in range(10):
    print ("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    
    if guess_row == ship_row or ship_row2 and guess_col == ship_col or ship_col2:
        print ('You hit my battleship!')
        board[guess_row][guess_col] = '0'
    if board[ship_row][ship_col] == '0' and board[ship_row2][ship_col2] == '0':
      print ("Congratulations! You sank my battleship!")
      break    
    else:
      if guess_row not in range(1,6) or \
      guess_col not in range(1,6):
        print ("Oops, that's not even in the ocean.")
      elif board[guess_row][guess_col] == "X" or '0':
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

print (play_game())