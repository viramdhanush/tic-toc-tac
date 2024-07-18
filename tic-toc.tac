import math

# Initialize the board
def initialize_board():
    return [' ' for _ in range(9)]

# Print the board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('|'.join(row))
        print('-' * 5)

# Check for a winner
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Check if the board is full
def is_board_full(board):
    return ' ' not in board

# Minimax algorithm with optional alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

# Get the best move for the AI
def get_best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop
def play_game():
    board = initialize_board()
    human = 'X'
    ai = 'O'
    
    while True:
        print_board(board)
        
        # Human move
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move! Try again.")
            continue
        board[move] = human
        
        if check_winner(board, human):
            print_board(board)
            print("You win!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # AI move
        ai_move = get_best_move(board)
        board[ai_move] = ai
        
        if check_winner(board, ai):
            print_board(board)
            print("AI wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

# Start the game
play_game(
