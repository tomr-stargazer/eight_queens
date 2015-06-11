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
