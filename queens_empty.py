# Solves the N-Queens problem:
# Place N queens on an N×N chessboard so that no two queens attack each other.
# Queens must not share the same row, column, or diagonal.
def is_safe(board, row, column):
    """
    Check whether a queen can be safely placed on board at position (row, column).

    The position is considered unsafe if there is already a queen in the same row, column or on the upper or lower diagonal. 
    
    Parameters:
        board (list of list): Current state of the chessboard.
        row (int): Row index.
        column (int): Column index.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    for j in range(column):
        if board[row][j] == 1:
            return False

    i, j = row, column
    while inBoundaries(board, i, j):
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, column
    while inBoundaries(board, i, j):
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def inBoundaries(board, row, column):
    return 0 <= row < len(board) and 0 <= column < len(board[0])

def print_board(board: list[list[int]]):
    """
    Print the current configuration of the chessboard.

    Representation:
        'X' → queen
        '.' → empty cell

    Each row is printed on a separate line.
    """
    out = ""

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                out += "."
            else:
                out += "X"
        out += "\n"
    print(out)

def solve_n_queens(n, one_solution = True):
    """
    Solve the N-Queens problem using backtracking.

    The algorithm incrementally builds the solution by placing queens
    column by column and backtracking when a conflict occurs.

    Parameters:
        n (int): Size of the board (n×n) (and number of queens).
        one_solution (bool):
            - True  → stop after finding the first valid solution
            - False → find and print all possible solutions

    Returns:
        int: Number of valid solutions found.
    """
    board =[]
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append(0)
    return placeQueen(board, 0, one_solution)


def placeQueen(board, column, oneSolution) -> int:
    if column == n:
        print_board(board)
        return 1

    solutions = 0

    for row in range(n):
        if is_safe(board, row, column):
            board[row][column] = 1
            solutions += placeQueen(board, column + 1, oneSolution)
            board[row][column] = 0
            if oneSolution and solutions == 1:
                return 1
    return solutions
# Example usage:
if __name__ == "__main__":          
    n = 5
    number_of_solutions = solve_n_queens(n, False)
    print(f"Total solutions found: {number_of_solutions}")

'''
Example output for n = 5 (all solutions):

X . . . . 
. . . X . 
. X . . . 
. . . . X
. . X . .

X . . . .
. . X . .
. . . . X
. X . . .
. . . X .

. . X . .
X . . . .
. . . X .
. X . . .
. . . . X

. . . X .
X . . . .
. . X . .
. . . . X
. X . . .

. X . . .
. . . X .
X . . . .
. . X . .
. . . . X

. . . . X
. . X . .
X . . . .
. . . X .
. X . . .

. X . . .
. . . . X
. . X . .
X . . . .
. . . X .

. . . . X
. X . . .
. . . X .
X . . . .
. . X . .

. . . X .
. X . . .
. . . . X
. . X . .
X . . . .

. . X . .
. . . . X
. X . . .
. . . X .
X . . . .

Total solutions found: 10

'''