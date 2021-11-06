class TTTBoard:


  #  The function below makes a Tic Tac Toe board 
  def __init__(self):
    self.board=[[1,2,3],[4,5,6],[7,8,9]]
  
  def display(self):
    for r in range(3):
      for c in range(3):
        if c>0: 
          print("|",end="")
        print(self.board[r][c],end="")
      print()
      if r<2: print("-----")


  def getLoc(self,n):
    for i,j in enumerate(self.board):
      if n in j:
        return [i,j.index(n)]
#The function return the value of rows and columns in the game

  def tryMove(self,m,p):
    for i,j in enumerate(self.board):
      if m in j:
        self.board[i][j.index(m)]=p
        return True
    print("This place is not available, please enter your choice again",end="\n")
    return False


  #The function will check if the user wins or not.
  def win(self):
    for i in self.board:
      if i[0]==i[1]==i[2]=="O":
        return "O Win"
      elif i[0]==i[1]==i[2]=="X":
        return "X Win"
    for j in range(3):
      if self.board[0][j]==self.board[1][j]==self.board[2][j]=="O":
        return "O Win"
      elif self.board[0][j]==self.board[1][j]==self.board[2][j]=="X":
        return "X Win"
    if self.board[0][0]==self.board[1][1]==self.board[2][2]=="O":
      return "O Win"
    if self.board[0][0]==self.board[1][1]==self.board[2][2]=="X":
      return "X Win"
    if self.board[0][2]==self.board[1][1]==self.board[2][0]=="O":
      return "O Win"
    if self.board[0][2]==self.board[1][1]==self.board[2][0]=="X":
      return "X Win"
