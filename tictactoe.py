# Tic Tac Toe
# by DKKO

def print_board(board_moves):
    # This process prints an ASCII tic tac toe table with the current values
    for i in range(3):
        print(f"  {board_moves[3*i]}  |  {board_moves[3*i+1]}  |  {board_moves[3*i+2]}")
        if not i == 2: # this way we avoid having - in the last row
            print("-"*17) 
    
    return None

# MAIN
def main():
    # Initialize list for the board values
    board_moves = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print_board(board_moves)

    # Game Loop
    playing = True
    player = "X"
    while playing:
        # Ask for the board position
        valid = False
        while not valid:
            try:
                position = int(input("Enter a number between 1-9 >>> ")) 
                if not (1 <= position <= 9):
                    raise ValueError
            except ValueError:
                print("MUST BE AN INTEGER BETWEEN 1-9")
            else:
                valid = True
        
        # Update the board
        board_moves[position-1] = player

        # Switch player
        if player == "X":
            player = "O"
        else:
            player = "X"

        # Loop break
        if not " " in board_moves:
            playing = False
        
        #Print the board at the end of the play
        print_board(board_moves)


if __name__ == "__main__":
    main()