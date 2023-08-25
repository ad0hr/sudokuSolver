from functions import *

board = [
    [0, 0, 1, 0, 0, 4, 6, 0, 2],
    [8, 2, 7, 1, 0, 3, 5, 0, 9],
    [0, 4, 9, 5, 2, 0, 0, 3, 0],
    [2, 0, 0, 0, 0, 0, 3, 9, 6],
    [7, 0, 0, 0, 1, 6, 0, 8, 4],
    [0, 0, 0, 3, 8, 2, 0, 5, 7],
    [0, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 8, 5, 2, 0, 0, 7, 6, 3],
    [0, 7, 4, 0, 5, 0, 9, 2, 8]
]

def test_correct():
    assert correct(board, 4, 6, 2) == True
    assert correct(board, 4, 6, 1) == False

def test_correct_square():
    assert correct(board, 5, 6, 1) == True
    assert correct(board, 5, 6, 8) == False