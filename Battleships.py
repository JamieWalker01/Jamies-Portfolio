from random import randint
from random import choice

board = []

for x in range(0, 6):
  board.append(["O"] * 6)

board[0][1:6] = ['1', '2', '3', '4', '5']
board[1][0] = '1'
board[2][0] ='2'
board[3][0] = '3'
board[4][0] = '4'
board[5][0] = '5'

def print_board(board):
  for row in board:
    print (" ".join(row))

def random_row(board):
  return randint(1, len(board) - 1)

def random_col(board):
  return randint(1, len(board[0]) - 1)

def add_rand_row(number):
    added_row = choice([number-1, number+1])
    if number == len(board)-1:
        added_row = len(board)-2
        return added_row
    elif number == 1:
        added_row = 2
        return added_row
    else:
        return added_row

def add_rand_col(number):
    added_col = choice([number-1, number+1])
    if number == len(board[0])-1:
        added_col = len(board[0])-2
        return added_col
    elif number == 1:
        added_col = 2
        return added_col
    else:
        return added_col

 
def play_game():

  board = []

  for x in range(0, 6):
    board.append(["O"] * 6)

  board[0][1:6] = ['1', '2', '3', '4', '5']
  board[1][0] = '1'
  board[2][0] ='2'
  board[3][0] = '3'
  board[4][0] = '4'
  board[5][0] = '5'

  ship_row = random_row(board)
  ship_col = random_col(board)
  temp_row = add_rand_row(ship_row)
  temp_col = add_rand_col(ship_col)

  new_cord = choice([temp_row, temp_col])
  if new_cord == temp_row:
    ship_row2 = new_cord
    ship_col2 = ship_col
  elif new_cord == temp_col:
    ship_row2 = ship_row 
    ship_col2 = new_cord

  print_board(board)
  print ('There is an enemy ship which covers 2 spaces.')
  print('It could be horizontal or vertical.')
  print('Can you help us find it!')
  for turn in range(10):
    print ("Turn", turn + 1)
    
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    
    if guess_row not in range(1,6) or \
        guess_col not in range(1,6):
        print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
        print("You guessed that one already.")
    elif board[guess_row][guess_col] == '0':
        print('You guessed that one already.')
    elif (guess_row == ship_row and guess_col == ship_col) or \
         (guess_row == ship_row2 and guess_col == ship_col2):
        print ('You hit my battleship!')
        board[guess_row][guess_col] = '0'
        print_board(board)
    else:
        print ("You missed my battleship!")
        board[guess_row][guess_col] = "X"
        print_board(board)
    if board[ship_row][ship_col] == '0' and board[ship_row2][ship_col2] == '0':
      print ("Congratulations! You sank my battleship!")
      rematch = input('Do you want a rematch?: ')
      if rematch == 'yes':
        print (play_game())
        break
      elif rematch == 'no':
        print ('OK, see ya!')
        break
      else:
          print ('Please type yes or no.')
          print(rematch)
    if turn == 9:
      print ('Game Over')
      rematch = input('Do you want a rematch?: ')
      if rematch == 'yes':
        print (play_game())
      elif rematch == 'no':
        print ('OK, see ya!')
        break
      else:
          print ('Please type yes or no.')
          print (rematch)

play_game()