"""
Ok, so let's attempt to solve the 8 queens problem. (like, brute-force-ly.)

My understanding of the eight queens problem: try to put 8 queens on a 
chess board that don't threaten each other chess-ly.

"""

import numpy as np

chess_board = np.zeros((8,8))

# let's try first an "eight rooks" problem?

def rook_threatened_squares(x, y, board=chess_board):
    """
    Takes a rook x,y position and returns the threatened squares as True.

    """

    x_indices, y_indices = np.indices(board.shape)

    # threatened squares are where either x or y is equal, but NOT BOTH (because that's the square you're on)
    threatened = (((x_indices == x) | (y_indices == y)) & 
                 ~((x_indices == x) & (y_indices == y)))

    return threatened

def queen_threatened_squares(x, y, board=chess_board):
    """
    Takes a queen x,y position and returns the threatened squares as True.

    """

    x_indices, y_indices = np.indices(board.shape)

    # threatened squares are where either 
    #   x is equal, or
    #   y is equal, or
    #   x+y is equal, or
    #   x-y is equal, 
    # AND:
    #   NOT x=x and y=y (because that's the square you're on)
    threatened = (((x_indices == x) | 
                   (y_indices == y) |
                   (x_indices+y_indices == x+y) |
                   (x_indices-y_indices == x-y)
                   ) & 
                 ~((x_indices == x) & (y_indices == y)))

    return threatened


def multiple_queens_threatened_squares(queen_positions):
    """
    Takes all queen positions and returns all threatened squares.

    Parameters
    ----------
    queen_positions : 2-d array
      Nonzero where a queen is

    """

    threatened = np.zeros_like(queen_positions)

    x_positions, y_positions = np.where(queen_positions != 0)

    for x, y in zip(x_positions, y_positions):

        threatened += queen_threatened_squares(x, y, board=queen_positions)

    return threatened.astype(np.bool)


def is_board_legal(queen_positions):
    """ 
    Checks if any of the queens threaten each other

    """

    threatened_squares = multiple_queens_threatened_squares(queen_positions)

    threatened_queens = (queen_positions.astype(np.bool) &
                         threatened_squares.astype(np.bool))

    if threatened_queens.any():
        return False
    else:
        return True


def eight_queen_solver(input_board=None, size=8):

    # initialize:
    if input_board is None:
        input_board = np.zeros((size, size))

    # check to see if we win:
    if ((np.sum(input_board.astype(np.bool)) == size) and 
        is_board_legal(input_board)):
        return input_board
    elif ((np.sum(input_board.astype(np.bool)) == size) and 
          ~is_board_legal(input_board)):
        raise ValueError("Somehow we got an illegal board as a result")

    threatened_squares = multiple_queens_threatened_squares(input_board)

    # check to see if we lose:
    if (input_board.astype(np.bool)+threatened_squares).all():
        return False

    # try all legal positions, put a queen there, and see how far we can get
    empty_unthreatened_squares = ~(input_board.astype(np.bool)+threatened_squares)
    x_positions, y_positions = np.where(empty_unthreatened_squares)

    for x, y in zip(x_positions, y_positions):

        queen_number = int(np.max(input_board)+1)

        print "Placing queen #{2} at ({0}, {1})".format(x, y, queen_number)

        board_with_new_queen = np.copy(input_board)
        board_with_new_queen[x, y] = queen_number

        result = eight_queen_solver(input_board=board_with_new_queen, size=size)

        if result is not False:
            return result
        else:
            print "Queen #{2} at ({0}, {1}) was a dead-end".format(x, y, queen_number)

    # exit this call with a False and let the next one proceed
    return False
