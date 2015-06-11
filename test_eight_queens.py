"""
Here are some tests for the eight_queens thing.

"""

import numpy as np
from numpy.testing import assert_equal

from .eight_queens import rook_threatened_squares, queen_threatened_squares

def test_rook_threatened_squares():

    # smaller cause I'm too lazy to type an expected 8x8 board
    test_board = np.zeros((3,3))

    expected_threatened = np.array([
        [False, True, False],
        [True, False, True],
        [False, True, False]
        ])

    threatened = rook_threatened_squares(1,1, board=test_board)

    assert_equal(threatened, expected_threatened)


def test_queen_threatened_squares():

    # smaller cause I'm too lazy to type an expected 8x8 board
    test_board = np.zeros((4,4))

    expected_threatened = np.array([
        [True, True, True, False],
        [True, False, True, True],
        [True, True, True, False],
        [False, True, False, True]        
        ])

    threatened = queen_threatened_squares(1,1, board=test_board)

    assert_equal(threatened, expected_threatened)

