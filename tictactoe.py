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

def minimax(maximizing, board):
    """
    Recursive game algorithm that has 2 Modes, Minimizing and Maximizing.

    Maximizing: AI's turn, it'll look for the move that gives the best outcome (win) or second best (draw)
    
    Minimizing: "Player's Turn" but in reality is the AI simulating the player. It'll try to make the AI lose by doing the move that gives the AI
    the worst outcome (lose).

    Since it's a tic-tac-toe game, we can use minimax until end-game, but usually you give it a depth of how many recursions it takes. 
    """
    #BASE CASE: game is finished
    if check_winner(board, "O"):
        return 10.0
    elif check_winner(board, "X"):
        return -10.0
    elif not " " in board:
        return 0.0

    moves = [index for index, tile in enumerate(board) if tile == " "]
    # GENERAL CASE
    if maximizing:
        best_move_score = float("-inf")
        for index in moves:
            board[index] = "O"
            move_score = minimax(False, board) # assign a score to that move. Call Minimizing
            board[index] = " " # Backtrack
            
            best_move_score = max(move_score, best_move_score)
        return best_move_score

    else: # Minimizing
        best_move_score = float("inf")
        for index in moves:
            board[index] = "X" 
            move_score = minimax(True, board) # Call Maximizing
            board[index] = " " # Backtrack

            best_move_score = min(move_score, best_move_score)
        return best_move_score            

def do_best_move(board):
    best_move_score = float("-inf")
    best_move = None
    
    avaliable_tiles = [index for index, tile in enumerate(board) if tile == " "]
    
    for tile in avaliable_tiles:
        board[tile] = "O"
        move_score = minimax(False, board) #We call minimax Maximizing, because it is AI's turn.
        board[tile] = " "

        if move_score > best_move_score:
            best_move_score = move_score
            best_move = tile

    board[best_move] = "O"
    return None

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
        if player == "O": #AI
            do_best_move(board)
        else: #HUMAN
            valid = False
            while not valid:
                try:
                    position = int(input("Enter a number between 1-9 >>> ")) 
                    if not (1 <= position <= 9):
                        raise ValueError
                    elif not board[position-1] == " ":
                        raise ValueError 
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