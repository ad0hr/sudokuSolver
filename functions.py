import numpy as np

board_sample = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(sudoku):
    """ takes a list of numbers representing an unsolved sudoku board and prints it out for visuals
    -----------
    parameters:
    sudoku (list)
        lists of int values in list that represents a sudoku board
    """
    for j in range(len(sudoku)):
        if j % 3 == 0 or j == 9:
            print("--------------")
        for i in range(len(sudoku[j])):
            if i % 3 == 0 or i == 0:
                print("|", end="")
                print(str(sudoku[j][i]), end="")
            elif i == 8:
                print(str(sudoku[j][i]), end="")
            else:
                print(str(sudoku[j][i]), end="")
        print("|")
    print("--------------")


def find_empty(sudoku):
    """
    goes through a given sudoku board to find the next empty place (denoted by 0) and returns the location
    ---------
    parameters:
    sudoku (list)
        lists of int values in list that represents a sudoku board
    ---------
    returns:
    r (int)
        row of empty space in sudoku board
    c (int)
        column of the empty space in sudoku board
    """

    for r in range(9):
        for c in range(9):
            if sudoku[r][c] == 0:
                return r, c
            
    # if there are no empty squares
    return False


def correct(sudoku, r, c, n):
    """
    checks if a number (n) can be placed at position specified (r,c) against the rules of sudoku
    --------
    parameters:
    sudoku (list)
        lists of int values in list that represents a sudoku board
    r (int)
        row position to place number
    c (int)
        column position to place number
    n (int)
        number to be placed
    --------
    returns:
    True (boolean)
        if the number can be placed at position, returns False otherwise
    --------
    notes:
        index is from 0 to 8
    """

    # checks if number does not already appear in the row
    for i in range(8):
        if sudoku[r][i] == n and c != i:
            return False

    # checks if number does not already appear in the column
    for j in range(8):
        if sudoku[j][c] == n and r != j:
            return False

    # checks if number does not already appear in its 3x3 square
    x = r // 3
    y = c // 3

    for i in range(x*3, x*3 + 3):
        for j in range(y*3, y*3 + 3):    
            if sudoku[i][j] == n and (i, j != r, c):
                return False
            
    return True

def solve(board):
    """
    solves a given sudoku board using backtracking
    ---------
    parameters:
    board (list)
        lists of int values in list that represents a sudoku board
    ---------
    returns:
    True (boolean)
        if the board is solved, returns False otherwise
    """

    # initialise the base case
    if not find_empty(board):
        # if there are no more empty squares then the sudoku is solved
        return True
    else:
        row, col = find_empty(board)

    # call solve function recursively to solve board
    for potential_sln in range(1,10):
        if correct(board, row, col, potential_sln):
            board[row][col] = potential_sln

            # 1) if the board has been solved 
            if solve(board):
                return True
            
            # if there are no more correct values (the potential sln was incorrect), reset the position value to 0
            board[row][col] = 0

    # 1) else, try again for position with new values
    return False