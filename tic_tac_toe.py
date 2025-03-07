
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Prompt for player's symbol until valid input is given
    while True:
        player = input("Enter your character (X or O): ").upper()
        if player not in ['X', 'O']:
            print("Please enter a valid character. Either X or O.")
        else:
            break
    
    while True:
        print(f"\nYou are playing as {player}")
        play_board(board)
        
        row, col = get_player_move(board)
        mark_move(row, col, board, player)
        
        if check_win(board, player):
            play_board(board)
            print("Congratulations! You win!")
            break
        
        if is_board_full(board):
            play_board(board)
            print("It's a draw!")
            break
        
        # Switch player (for two-player game, or if you plan to add a computer move later)
        player = 'O' if player == 'X' else 'X'
    
def play_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def get_player_move(board):
    # Loop until valid row and column are provided
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
        except ValueError:
            print("Enter only numbers (0, 1, or 2).")
            continue
        
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Row and column must be between 0 and 2.")
            continue
        if board[row][col] != " ":
            print("That cell is already taken. Please choose another one.")
            continue
        
        return row, col

def mark_move(row, col, board, player):
    board[row][col] = player

def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Start the game
tic_tac_toe()
