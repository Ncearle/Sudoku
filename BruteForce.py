"""
Brute Force method for solving Sudoku puzzles

This approach takes a partial Sudoku and the goes through
all possible configurations until one is found.
"""

import numpy as np


def printBoard(board):
    """
    :param board: Sudoku board
    :return: Prints out a Sudoku board
    """
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
            if (j+1) % 3 == 0 and j < 8:
                print("|", end=" ")
        print()
        if (i+1) % 3 == 0 and i < 8:
            print("-"*21)
    print()


def isValid(board, row, col, num):
    """
    Checks the cell's "cross" for the num to see if it is valid. The cross
    is the row, column, and 3x3 box in which we find the current cell
    :param board: The Sudoku board
    :param row: Row
    :param col: Column
    :param num: potential number for cell
    :return: Whether or not we can put that number in i,j
    """
    # Check for the num in the same row
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check for the num in the same column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check for num in the mini-board
    startRow = row - (row % 3)  # Top left cell for 3x3 mini-board
    startCol = col - (col % 3)
    for i in range(3):
        for j in range(3):
            if board[startRow+i][startCol+j] == num:
                return False

    return True


def solveSudoku(board, row=0, col=0):
    """
    The naive brute-force method for solving a Sudoku. Tries every configuration,
    until we find one that works.
    :param board: Your sudoku board
    :param row: current row, set to 0
    :param col: current col, set to 0
    :return: Solved Sudoku board
    """
    N = 9
    # Check to see if we have reached the final cell
    if row == N - 1 and col == N:
        return True

    # Check to see if we have reached the end of the row
    if col == N:
        row += 1
        col = 0

    # If the current position is filled, iterate for next column
    if board[row][col] > 0:
        return solveSudoku(board, row, col+1)

    # Iterate to find next value
    for num in range(1, 10):
        # Check to see if its valid
        if isValid(board, row, col, num):
            # Assign num to the cell
            board[row][col] = num
            # Then continue to the next one
            if solveSudoku(board, row, col+1):
                return True

        # Didn't work out this time so we reset and try again
        board[row][col] = 0
    return False


if __name__ == "__main__":

    sudoku = np.array([[9, 0, 2, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 9, 0, 5, 2, 3, 0],
                       [0, 8, 0, 0, 0, 0, 6, 0, 9],
                       [4, 0, 0, 0, 2, 0, 7, 5, 0],
                       [0, 1, 0, 5, 9, 8, 0, 6, 0],
                       [0, 5, 3, 0, 1, 0, 0, 0, 8],
                       [8, 0, 9, 0, 0, 0, 0, 4, 0],
                       [0, 7, 6, 1, 0, 2, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 3, 0, 2]])

    printBoard(sudoku)
    solveSudoku(sudoku)
    printBoard(sudoku)
