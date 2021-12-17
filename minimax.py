import copy
from typing import Tuple, Optional

from board import TicTacToeBoard


def evaluate(board: TicTacToeBoard) -> int:
    return -1 if board.is_finished() and board.winner() is not None else 0


def minimax(board: TicTacToeBoard, max_depth: int = 6, depth: int = 0) -> Tuple[int, Optional[int]]:
    if board.is_finished() or depth == max_depth:
        return evaluate(board), None

    best_score = None
    best_move = None
    for move in board.possible_moves():
        new_board = copy.deepcopy(board)
        new_board.move(move)
        score, next_move = minimax(new_board, max_depth, depth + 1)
        score = -score
        if best_score is None or score > best_score:
            best_score = score
            best_move = move

    return best_score, best_move
