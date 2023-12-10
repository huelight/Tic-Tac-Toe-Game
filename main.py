def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ' or board[0][i] == board[1][i] == board[2][i] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False


def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)


def tic_tac_toe():
    # Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    # Initialize player
    current_player = 'X'

    while True:
        print_board(board)

        # Get player move with input validation
        while True:
            try:
                row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
                col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Update the board
        board[row][col] = current_player

        # Check for a winner
        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    tic_tac_toe()
