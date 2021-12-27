grid = [[[] for i in range(3)] for j in range(3)] #creates a grid in range of 3x3

from random import randint #import random.randint from random module

#Function to print the grid, so we each time we need to print the grid we just call the function
def print_grid():
  print('   1    2    3')
  print('1  {} | {} | {}'.format(grid[0][0], grid[0][1], grid[0][2])) #use .format() to use simple placeholders for the position
  print('   ------------')
  print('2  {} | {} | {}'.format(grid[1][0], grid[1][1], grid[1][2]))
  print('   ------------')
  print('3  {} | {} | {}'.format(grid[2][0], grid[2][1], grid[2][2]))

#Function to display whos turn it is
def player_input(player):
  input_is_correct = False

  if 'player one' in player: #checking to see if its player ones turn, if it is display player ones turn and assign symbol
    print("Player One's turn")
    player_symbol='X'

  else:
    print("Player Two's turn") #if it is not player 1's turn, it will default to player twos turn
    player_symbol='O'
  player_row = input('Enter the row:')

  if player_row.isdigit(): #checks to see if user input is a digit
    player_row = int(player_row)-1
    if player_row < 3: #if the user input is less than 3, set correct to True
      input_is_correct = True # if the user input is less than 3, the while loop below will be skipped and will go straight to asking for the column

  while not input_is_correct: #while loop to keep asking the user to enter a number between 1 and 3 if it is not in the range
    print("Player row must be a number between 1 and 3..")
    player_row = input('Enter the row:')

    if player_row.isdigit(): #checks again if the user entered a digit
      player_row = int(player_row)-1
      if isinstance(player_row, int): #checks to see if user input is an integer
        if player_row < 3:
          input_is_correct = True #if correct answer given, input_is_correct = False and column will be asked

  input_is_correct = False
  player_column = input('Enter the column: ') #When the user enters the correct row, it will break out of the loop and ask to enter a column

  if player_column.isdigit(): #checks again to see if user input is a digit
    player_column = int(player_column)-1
    if player_column < 3: 
      input_is_correct = True #if user input is less than 3, while loop below will be skipped and will proceed to display a grid

  while not input_is_correct: #perform same checks as column to ensrue player input is within boundaries
    print("Player row must be a number between 1 and 3..")
    player_column = input('Enter the column: ')
    if player_column.isdigit(): #checks again if the user entered a digit
      player_column = int(player_column)-1
      if isinstance(player_column, int): #checks to see if user input is an integer
        if player_column < 3:
          input_is_correct = True #if correct answer given, input_is_correct = False and column will be asked
  
  while True: #while it is true, and user has made no mistakes, display the grid
    if len(grid[player_row][player_column]) < 1: #when the player enters the correct position, the grid will be displayed and updated
      grid[player_row][player_column] = player_symbol
 
      break #stops the grid from continously showing
    else:
      print('The space you chose is occupied, please choose another space.') #displays message when user inputs in an occupied space
      player_row = int(input('Enter the row:')) - 1
      player_column = int(input('Enter the column: ')) - 1

def run_game():

  print('Before starting, let\'s throw a coin to see which player goes first and what symbol each player will use:') #implementing a coin toss method for players to choose what symbol to use
  print('The coin has the number 1 on one side and a number 2 on the other side.')
  print()
  print('The player who wins the coin toss will use an \'X\' and the other player will use \'O\'.')
  print()
  player_one_coin_pick = int(input('Player One choose 1 or 2 for coin toss:'))
  coin_flip = randint(1,2) #randomises 2 values for the coin toss
  print()
  if coin_flip == player_one_coin_pick: 
    print("Coin toss returned " + str(coin_flip) +", which means player one will start and will use 'X' and player two will use 'O'.") #display results of random value
    player1_symbol = 'X' #assigns player symbols
    player2_symbol = 'O'

  else:
    print("Coin toss returned " + str(coin_flip) +", which means player two will start and will use 'X' and player one will use 'O'.") #displays alternative random value
    player1_symbol = 'O'
    player2_symbol = 'X'

  print_grid() #Function to print the grid, so we each time we need to print the grid we just call the function
  print()
  
  finished = False #Variable to keep the loop executing while neither player has won or there's at least one space left to play
  spaces_used = 0 #Number of spaces used by the player; could also be interpreted as number of total plays

  while not finished: #Main loop to run the game while the game is not finished
    
    if player1_symbol == 'X':
      player_input('player one') #displays which player is playing

    else:
      player_input('player two')
    print()
    print_grid()
    print()

    #Test if all spaces have been used
    if spaces_used == 9: #if all 9 boxes are filled and no one won, it will be a draw
      print('Game was a draw!')
      finished = True
      break

    #finding possible ways player 1 can win
    #Test if Player 1 won by completing a row
    if (grid[0][0] == grid[0][1] == grid[0][2] != []) or (grid[1][0] == grid[1][1] == grid[1][2] != []) or (grid[2][0] == grid[2][1] == grid[2][2] != []):
      print('Player 1 has won!')
      finished = True
      break
    #Test if Player 1 won by completing a column
    if (grid[0][0] == grid[1][0] == grid[2][0] != []) or (grid[0][1] == grid[1][1] == grid[2][1] != []) or (grid[0][2] == grid[1][2] == grid[2][2] != []):
      print('Player 1 has won!')
      finished = True
      break
    #Test if Player 1 won by completing the left diagonal
    if grid[0][0] == grid[1][1] == grid[2][2] != []:
      print('Player 1 has won!')
      finished = True
      break
    #Test if Player 2 won by completing the right diagonal
    if grid[0][2] == grid[1][1] == grid[2][1] != []:
      print('Player 1 has won!')
      finished = True
      break

    #Player 2 inputs
    
    if player1_symbol == 'O':
      player_input('player one')
    else:
      player_input('player two')
    print()
    print_grid()
    print()
    # print('spaces_used:', spaces_used)

    #Test if all spaces have been used
    if spaces_used == 9:
      print('Game was a draw!')
      finished = True
      break
    #Test if Player 2 won by completing a row
    if (grid[0][0] == grid[0][1] == grid[0][2] != []) or (grid[1][0] == grid[1][1] == grid[1][2] != []) or (grid[2][0] == grid[2][1] == grid[2][2] != []):
      print('Player 2 has won!')
      finished = True
      break
    #Test if Player 2 won by completing a column
    if (grid[0][0] == grid[1][0] == grid[2][0] != []) or (grid[0][1] == grid[1][1] == grid[2][1] != []) or (grid[0][2] == grid[1][2] == grid[2][2] != []):
      print('Player 2 has won!')
      finished = True
      break
    #Test if Player 2 won by completing the left diagonal
    if grid[0][0] == grid[1][1] == grid[2][2] != []:
      print('Player 2 has won!')
      finished = True
      break
    #Test if Player 2 won by completing the right diagonal
    if grid[0][2] == grid[1][1] == grid[2][1] != []:
      print('Player 2 has won!')
      finished = True
      break

while(True):
  grid = [[[] for i in range(3)] for j in range(3)]
  run_game() 
  play_again = input("Do you want to play again?") #after the game has finished playing, ask user if they wanna play again. if player says "yes", main game function will be called and game will start again
  if play_again.lower() != "yes" and play_again.lower() != "y": #ensures that if the user enters upper case "yes" or lower case, it will still be accepted
    print("\nGoodbye! Thanks for playing the game!")
    break
