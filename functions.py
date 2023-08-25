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

    for r in range(8):
        for c in range(8):
            if sudoku[r][c] == 0:
                return r, c


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
        if sudoku[r][i] == n:
            return False

    # checks if number does not already appear in the column
    for j in range(8):
        if sudoku[j][c] == n:
            return False

    # checks if number does not already appear in its 3x3 square
    for i in range(r, r + 2):
        for j in range(c, c + 2):
            if sudoku[i][j] == n:
                return False
    return True


