#The program is made by Nifu Dan and will play a tic tac toe game for users.
from TTTBoard import TTTBoard



def player(i):
  if i%2==0:
    return "X"
  else:
    return "O"
#The function above will return X or O


def test():
  try:
    global posN
    global p
    posN=int(input(f"{p} enter you move (1-9): "))
    print()
    if posN not in range(1,10):
      print("Move must be in range 1-9!")
      test()
    return
  except ValueError:
    print()
    print("Please enter a number!")
    test()
#The funtion above tests the range that users enter, and will check whether the entered number fulfill the requirment of the program.

def TTT():
  board=TTTBoard()
  board.display()
  for i in range(1,10):
    global posN
    global p
    p=player(i)
    print()
   
    test()
    succ=False
    while not succ:
      if board.tryMove(posN,p):
        print()
        succ=True
      else:
        test()
    board.display()
    winner = board.win()
    if winner != None:
      print()
      print(f"{p} wins! congratulation!")
      break
    elif i==9 and winner==None:
      print()
      print("Tie")
#The function above will create the game and the function below runs the main function.

TTT()
