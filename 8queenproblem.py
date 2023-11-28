def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_solution(board):
    for row in board:
        line = ['Q' if i == row else '.' for i in range(8)]
        print(' '.join(line))
    print("\n")

def solve_queens(board, row):
    if row == 8:
        # All queens are placed, print the solution
        print_solution(board)
        return

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            solve_queens(board, row + 1)
            board[row] = 0  # backtrack

def solve_8_queens():
    board = [0] * 8
    solve_queens(board, 0)

if __name__ == "__main__":
    solve_8_queens()
