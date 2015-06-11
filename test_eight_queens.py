"""
Here are some tests for the eight_queens thing.

"""

import numpy as np
from numpy.testing import assert_equal

from .eight_queens import (
    rook_threatened_squares, queen_threatened_squares,
    multiple_queens_threatened_squares, is_board_legal)


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


def test_multiple_queens_threatened_squares():

    queen_positions = np.array([
        [0, 0, 2, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0]])

    expected_threatened = np.array([
        [1, 1, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 0],
        [1, 0, 1, 1]]).astype(np.bool)

    threatened = multiple_queens_threatened_squares(queen_positions)

    assert_equal(threatened, expected_threatened)


def test_is_board_legal():

    queen_positions_1 = np.array([
        [0, 0, 2, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0]])

    assert is_board_legal(queen_positions_1)

    queen_positions_2 = np.array([
        [0, 0, 2, 0],
        [0, 0, 0, 3],
        [0, 0, 0, 0],
        [0, 1, 0, 0]])

    assert ~is_board_legal(queen_positions_2)

    queen_positions_3 = np.array([
        [0, 0, 2, 0],
        [4, 0, 0, 0],
        [0, 0, 0, 3],
        [0, 1, 0, 0]])

    assert is_board_legal(queen_positions_3)

    queen_positions_4 = np.array([
        [0, 0, 2, 0, 0],
        [3, 0, 0, 0, 0],
        [0, 0, 0, 4, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 5]])

    assert is_board_legal(queen_positions_4)

    queen_positions_5 = np.array([
        [1,0],
        [2,3]])

    assert ~is_board_legal(queen_positions_5)

