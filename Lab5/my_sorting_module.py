'''
Author: Pratik kulkarni

This program sorts the board using Quick sort algorithm in descending order.
'''

def sortBoard(board, start, end):
    '''
    This method will sort the board using Quick sort.
    :param board:     The board to sort
    :param start:     The starting index for the sort
    :param end:       The last index for the sort
    :return:          NONE (As we are updating the board itself)
    '''
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right and left <= end and right >= start:
        if board[pivot].sum < board[left].sum:
            left += 1
        elif board[right].sum <= board[pivot].sum:
            right -= 1
        else:
            board[left], board[right] = board[right], board[left]
    board[pivot], board[right] = board[right], board[pivot]
    sortBoard(board, start, right)
    sortBoard(board, right+1, end)
