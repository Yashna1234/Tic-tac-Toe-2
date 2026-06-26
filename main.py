import random 

board=[" "for _ in range (9)]

def print_board():
     print("\nCurrent Board: ")
     for i in range(3):
          row = " | " .join(board[j + i * 3] for j in range (3))
          print(row)
          if i < 2:
               print("---+---+---")

def check_winner(b,player):
     win_condition=[
          (0,1,2),(3,4,5),(6,7,8),
          (0,3,6),(1,4,7),(2,5,8),
          (0,4,8),(2,4,6)
     ]
     return any(b[i] == b[j] == b[k] == player for i,j,k in win_condition)

def is_draw(b):
     return " " not in b

def ai_move():
     for i in range(9):
          if board[i]== " ":
               board[i]="O"
               if check_winner(board,"0"):
                    print("\nAI made a winning move.")
                    print_board()
                    return
               board[i] = " "

     for i in range(9):
          if board[i]== " ":
               board[i]="X"
               if check_winner(board,"X"):
                    board[i]="O"
                    print("\nAI blocked your move.")
                    print_board()
                    return
               board[i] = " "

     move=random.choice([i for i in range(9) if board[i] ==" "])
     board[move]="O"
     print("\nAI made a random move")
     print_board()

def player_move():
     while True:
        try:
               pos = int(input("Enter your move (1-9): ")) - 1
               if 0 <= pos < 9 and board[pos] == " ":
                    board[pos] = "X"
                    print("\nYou made your move.")
                    print_board()
                    break
               else:
                    print("Invalid move. Try again.")
        except ValueError:
             print("Please enter a number between 1 and 9.")
     
def play_game():
     print("Welcome to Tic-Tac Toe!")
     print_board()
     while True:
        player_move
        if check_winner(board, "X"):
             print("Congratulations! You Win!")
             break
        
        if is_draw(board):
             print("Its a draw!")
             break
        
        ai_move()
        if check_winner(board,"O"):
             print("AI wins! Beter luck next time.")
             break
        if is_draw(board):
             print("Its a draw!")
             break
        
if __name__=="__main__":
     play_game()
        
     
    