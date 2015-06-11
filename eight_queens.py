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
    Takes an x,y position and returns the threatened squares as True.

    """

    x_indices, y_indices = np.indices(board.shape)

    # threatened squares are where either x or y is equal, but NOT BOTH (because that's the square you're on)
    threatened = (((x_indices == x) | (y_indices == y)) & 
                 ~((x_indices == x) & (y_indices == y)))

    return threatened

