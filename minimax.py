import copy
from typing import Tuple, Optional, Dict

from board import TicTacToeBoard

INFINITY = 1000


def evaluate(board: TicTacToeBoard) -> int:
    return -1 if board.is_finished() and board.winner() is not None else 0


def minimax(board: TicTacToeBoard,
            transposition_table: Dict[int, Tuple[int, Optional[int]]],
            max_depth: int = 9,
            depth: int = 0,
            alpha: int = -INFINITY,
            beta: int = INFINITY) -> Tuple[int, Optional[int]]:
    if board.hash() in transposition_table:
        return transposition_table[board.hash()]

    if board.is_finished() or depth == max_depth:
        result = evaluate(board), None
        transposition_table[board.hash()] = result
        return result

    best_score = -INFINITY
    best_move = None
    for move in board.possible_moves():
        new_board = copy.deepcopy(board)
        new_board.move(move)
        score, next_move = minimax(new_board, transposition_table, max_depth, depth + 1, -beta, -max(alpha, best_score))
        score = -score
        if score > best_score:
            best_score = score
            best_move = move

        if best_score >= beta:
            break

    result = best_score, best_move
    transposition_table[board.hash()] = result
    return result
