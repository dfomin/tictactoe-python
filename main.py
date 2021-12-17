from board import TicTacToeBoard


def main():
    board = TicTacToeBoard()
    while not board.is_finished():
        print(board)
        print(f"Current player: {board.current_player()}, possible moves: {board.possible_moves()}")
        try:
            position = int(input())
            board.move(position)
        except (ValueError, TypeError) as e:
            print(e)
    print(board)
    print(f"Winner is {board.winner()}")


if __name__ == '__main__':
    main()
