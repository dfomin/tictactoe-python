import numbers
import random

import numpy as np

BOARD_SIZE = 9

BOARD_PATHS = [
    (0, 1),
    (3, 1),
    (6, 1),
    (0, 3),
    (1, 3),
    (2, 3),
    (0, 4),
    (2, 2)
]


class TicTacToeBoard:
    def __init__(self, board: np.array = np.zeros(BOARD_SIZE, dtype=int), current_player: int = 0):
        if board.shape != (BOARD_SIZE,):
            raise ValueError("Wrong board size")

        self._board = board
        self._is_finished = False
        self._winner = None
        self._player_index = current_player
        self._hash_cache = 0

        self.check_end_game()

    def __repr__(self):
        result = ""
        for i in range(3):
            for j in range(3):
                value = self._board[i * 3 + j]
                if value == 1:
                    result += "X"
                elif value == 2:
                    result += "O"
                else:
                    result += " "
                if j < 2:
                    result += "|"
            if i < 2:
                result += "\n-----\n"
        return result

    def update_hash(self):
        self._hash_cache = 0
        for value in self._board:
            self._hash_cache += value
            self._hash_cache *= 3

    def hash(self):
        return self._hash_cache

    def move(self, position: int):
        if self.is_finished():
            raise ValueError("Game is over")

        if isinstance(type(position), numbers.Integral):
            raise TypeError(f"Position must be int, {type(position)} was given")

        if position not in self.possible_moves():
            raise ValueError(f"Position: {position} is unavailable, available positions: {self.possible_moves()}")

        self._board[position] = self._player_index + 1
        self._player_index = 1 - self._player_index

        self.update_hash()

        self.check_end_game()

    def possible_moves(self) -> np.array:
        if self.is_finished():
            return np.array([])
        return np.arange(BOARD_SIZE)[self._board == 0]

    def check_end_game(self):
        for path in BOARD_PATHS:
            indices = np.arange(path[0], path[0] + 3 * path[1], path[1])
            for i in range(2):
                if (self._board[indices] == i + 1).all():
                    self._is_finished = True
                    self._winner = i
                    return

        self._is_finished = (self._board != 0).all()

    def is_finished(self):
        return self._is_finished

    def current_player(self) -> int:
        return self._player_index

    def winner(self) -> int:
        return self._winner
