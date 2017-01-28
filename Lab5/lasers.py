'''
Author: Pratik kulkarni

This program will find the position and orientation of the lasers in the given
grid. For this we will first read the file that has the grid and stores it in a
2-dimensional list. The we find all possible orientations at all the positions
and select best out of them. Then we sort them based on the value of sum.
After sorting we can return position and orientation of the lasers.
'''

import sys
import collections
import my_sorting_module

FACE = ['North', 'East', 'South', 'West']
Orientation = collections.namedtuple("Orientation", ['row',
                                                     'column',
                                                     'orientationNumber', 'sum'])

def takeInput():
    '''
    This function will take input as fileName where grid is saved and number of
    lasers to place in that grid.
    :return:    a tuple of filehandle and number of lasers to be placed.
    '''
    fileName = input("Enter file name of the grid: ")
    try:
        fileHandle = open(fileName)
    except FileNotFoundError:
        print("Invalid file")
        sys.exit(0)
    numberOfLasers = input("Enter number of lasers to place in the grid: ")
    if numberOfLasers.isalpha():
        print("Invalid number")
        sys.exit(0)
    numberOfLasers = int(numberOfLasers)
    return fileHandle, numberOfLasers

def main():
    '''
    The main program.
    It takes input from the user. Then saves the grid from the file to a 2-d list
    Then finds all possible orientations on the board and selects the best at
    given position. Then it sorts the list having the orientations and prints
    the result.
    :return: NONE
    '''
    fileHandle, numberOfLasers = takeInput()
    board = makeBoard(fileHandle)
    boardWithOrientations = makeBoardWithOrientation(board)
    boardWithOrientations = cleanBoard(boardWithOrientations)
    my_sorting_module.sortBoard(boardWithOrientations, 0,
                                len(boardWithOrientations) - 1)
    ans = boardWithOrientations[:numberOfLasers]
    printResult(ans)


def printResult(ans):
    '''
    This method prints the result in the format
    (<column>, <row>) facing <direction>
    :param ans: The list containing result
    :return: NONE
    '''
    for element in ans:
        face = getDirection(element[2])
        print('(',element[1],',',element[0],')',' facing ',face)


def getDirection(face):
    '''
    Returns the direction based on value of face. It uses FACE list which stores
    the directions.
    :param face:     The numeric value for particular direction
    :return:    String for the numeric value for particular direction
    '''
    return FACE[face-1]


def makeBoardWithOrientation(board):
    '''
    This method will find out the best orientation possible at a given position
    .It stores the best orientations in a new list and returns that list.
    :param board:    The 2-d grid of numbers
    :return:    a list with best orientations for every position
    '''
    rows = len(board)
    columns = len(board[0])
    boardWithOrientation = list()
    for row in range(rows):
        for column in range(columns):
            orientations = getOrientations(row, column, board)
            boardWithOrientation.append(orientations)
    return boardWithOrientation


def makeBoard(fileHandle):
    '''
    This method will read the file using the fileHandle and copy the grid into
    a 2-d list and return that list.
    :param fileHandle:     File handle to read the data file
    :return:               The 2-d list which holds the grid as given in file
    '''
    board = list()
    for line in fileHandle:
        line = line.strip()
        row = line.split(' ')
        board.append(row)
    return board


def incrementPossible(maxNumber, entity):
    '''
    This method will check if its possible to increment the entity given maxNumber
    as upper bound.
    :param maxNumber:     The upper bound for entity
    :param entity:        The entity to check for increment
    :return:              True if we can increment the entity else False
    '''
    return entity + 1 < maxNumber


def decrementPossible(minNumber, entity):
    '''
    This method will check if its possible to decrement the entity given minNumber
    as lower bound.
    :param minNumber:     The lower bound for entity
    :param entity:        The entity to check for decrement
    :return:              True if we can decrement the entity else False
    '''
    return entity - 1 >= minNumber


def checkOrientationOne(row, column, board):
    '''
    This method will check if we can place the laser at given position in
    orientation one ie. facing North
    If yes it will return a tuple indicating orientation and sum of the lasers
    in that orientation. if its not possible to place the laser it will return
    (0, 0)
    :param row:    The row number of the element
    :param column: The column number of the element
    :param board:  The 2-d list (grid)
    :return:       Tuple indicating orientation and sum
    '''
    maxColumns = len(board[0])
    if (decrementPossible(0, row) and decrementPossible(0, column)
        and incrementPossible(maxColumns, column)):
        sum = int(board[row - 1][column]) + int(board[row][column - 1]) + \
              int(board[row][column + 1])
        return 1, sum
    else:
        return 0, 0


def checkOrientationTwo(row, column, board):
    '''
    This method will check if we can place the laser at given position in
    orientation two ie. facing East
    If yes it will return a tuple indicating orientation and sum of the lasers
    in that orientation. if its not possible to place the laser it will return
    (0, 0)
    :param row:    The row number of the element
    :param column: The column number of the element
    :param board:  The 2-d list (grid)
    :return:       Tuple indicating orientation and sum
    '''
    maxColumns = len(board[0])
    maxRows = len(board)
    if (decrementPossible(0, row) and incrementPossible(maxRows, row)
        and incrementPossible(maxColumns, column)):
        sum = int(board[row - 1][column]) + int(board[row + 1][column]) + \
              int(board[row][column + 1])
        return 2, sum
    else:
        return 0, 0


def checkOrientationThree(row, column, board):
    '''
    This method will check if we can place the laser at given position in
    orientation three ie. facing South
    If yes it will return a tuple indicating orientation and sum of the lasers
    in that orientation. if its not possible to place the laser it will return
    (0, 0)
    :param row:    The row number of the element
    :param column: The column number of the element
    :param board:  The 2-d list (grid)
    :return:       Tuple indicating orientation and sum
    '''
    maxColumns = len(board[0])
    maxRows = len(board)
    if (decrementPossible(0, column) and incrementPossible(maxColumns, column)
        and incrementPossible(maxRows, row)):
        sum = int(board[row][column - 1]) + int(board[row][column + 1]) + \
              int(board[row + 1][column])
        return 3, sum
    else:
        return 0, 0


def checkOrientationFour(row, column, board):
    '''
    This method will check if we can place the laser at given position in
    orientation four ie. facing West
    If yes it will return a tuple indicating orientation and sum of the lasers
    in that orientation. if its not possible to place the laser it will return
    (0, 0)
    :param row:    The row number of the element
    :param column: The column number of the element
    :param board:  The 2-d list (grid)
    :return:       Tuple indicating orientation and sum
    '''
    maxColumns = len(board[0])
    maxRows = len(board)
    if (decrementPossible(0, column) and incrementPossible(maxRows, row)
        and decrementPossible(0, row)):
        sum = int(board[row][column - 1]) + int(board[row - 1][column]) + \
              int(board[row + 1][column])
        return 4, sum
    else:
        return 0, 0


def getOrientations(row, column, board):
    '''
    This method will check all the orientations for the specified position
    (position is specified by row and column). then it will choose the best
    orientation out of all.
    It will return a new tuple Orientation(row, column, orientation, sum)
    :param row:    The row number of the element
    :param column: The column number of the element
    :param board:  The 2-d list (grid)
    :return:       Orientation(row, column, orientation, sum)
    '''
    orientations = list()
    orientations.append(checkOrientationOne(row, column, board))
    orientations.append(checkOrientationTwo(row, column, board))
    orientations.append(checkOrientationThree(row, column, board))
    orientations.append(checkOrientationFour(row, column, board))
    bestOrientation = getBestOrientation(orientations)
    return Orientation(row, column, bestOrientation[0], bestOrientation[1])


def getBestOrientation(orientations):
    '''
    This method finds out the best orientation based on the value of sum for
    that orientation.
    :param orientations:    The list of orientations for a position
    :return:                a tuple indicating orientationNumber and sum
    '''
    maxSum = 0
    number = 0
    for orientation in orientations:
        if orientation[0] > 0 and orientation[1] > maxSum:
                number = orientation[0]
                maxSum = orientation[1]
    return number, maxSum


def cleanBoard(board):
    '''
    It will remove all the orientations that are not valid.
    i.e. if the orientation is not possible it will remove it from the list
    Using this we get only valid orientations to sort from.
    :param board:     The list with all the orientations for whole grid
    :return:          A new list with no in-valid orientations
    '''
    newBoard = list()
    for index in range(len(board)):
        if not board[index].orientationNumber == 0:
            newBoard.append(board[index])
    return newBoard

if __name__ == '__main__':
    main()
