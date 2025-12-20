# Tic Tac Toe
# by DKKO

def print_board(board):
    # This process prints an ASCII tic tac toe table with the current values
    for i in range(3):
        print(f"  {board[3*i]}  |  {board[3*i+1]}  |  {board[3*i+2]}")
        if not i == 2: # this way we avoid having - in the last row
            print("-"*17) 
            
    return None

def check_winner(board, player):
    winning_indexes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    for idx in winning_indexes:
        if board[idx[0]] == player and board[idx[1]] == player and board[idx[2]] == player:
            return True
    
    return False

# MAIN
def main():
    # Initialize list for the board
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print_board(board)

    # Game Loop
    playing = True
    player = "X"
    while playing:
        # Ask for the board position and update it if empty
        valid = False
        while not valid:
            try:
                position = int(input("Enter a number between 1-9 >>> ")) 
                if not (1 <= position <= 9):
                    raise ValueError
                elif not board[position-1] == " ":
                    raise AssertionError 
            except ValueError:
                print("MUST BE AN INTEGER BETWEEN 1-9")
            except AssertionError:
                print("TILE IS OCCUPIED")
            else:
                valid = True

        board[position-1] = player

        # Check Winner
        player_won = check_winner(board, player)

        # Loop break
        if player_won:
            print_board(board)
            print(f"Player: {player} won")
            playing = False
        elif not " " in board:
            print_board(board)
            print("There's a Draw")
            playing = False
        else:
            # Print the board at the end of the play
            print_board(board)

        # Switch player
        if player == "X":
            player = "O"
        else:
            player = "X"

if __name__ == "__main__":
    main()