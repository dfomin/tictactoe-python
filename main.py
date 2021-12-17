import numpy as np

from board import TicTacToeBoard
from minimax import minimax


def main():
    try:
        board = TicTacToeBoard()
    except ValueError as e:
        print(e)

    while not board.is_finished():
        print(board)
        print(f"Current player: {board.current_player()}, possible moves: {board.possible_moves()}")
        best_score, best_move = minimax(board)
        print(f"Best score: {best_score}, best move: {best_move}")
        try:
            position = int(input())
            board.move(position)
        except (ValueError, TypeError) as e:
            print(e)

    print(board)
    print(f"Winner is {board.winner()}")


if __name__ == '__main__':
    main()
