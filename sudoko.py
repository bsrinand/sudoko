def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or board[row//3*3+i//3][col//3*3+i%3] == num:
            return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

sudoku_board = [[5, 3, 0, 0, 7, 0, 0, 0, 0], ...]  # Fill in with your board
solve_sudoku(sudoku_board)
print(sudoku_board)
