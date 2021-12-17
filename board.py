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
    def __init__(self):
        self._board = np.zeros(BOARD_SIZE)
        self._is_finished = False
        self._winner = None
        self._player_index = 0

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

    def move(self, position: int):
        if self.is_finished():
            raise ValueError("Game is over")

        if not type(position) is int:
            raise TypeError("Position must be int")

        if position not in self.possible_moves():
            raise ValueError(f"Position: {position} is unavailable, available positions: {self.possible_moves()}")

        self._board[position] = self._player_index + 1
        self._player_index = 1 - self._player_index

        self.check_end_game()

    def possible_moves(self) -> np.array:
        if self.is_finished():
            return np.array([])
        return np.arange(BOARD_SIZE)[self._board == 0]

    def check_end_game(self):
        for path in BOARD_PATHS:
            indices = np.arange(path[0], BOARD_SIZE, path[1])
            for i in range(2):
                if (self._board[indices] == i + 1).all():
                    self._is_finished = True
                    self._winner = i
                    return

    def is_finished(self):
        return self._is_finished

    def current_player(self) -> int:
        return self._player_index

    def winner(self) -> int:
        return self._winner
