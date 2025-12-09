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

if __name__ == "__main__":
    main()