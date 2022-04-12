from abc import abstractmethod
from Game.Board.board import Board
from Game.AI.position_points import get_position_points

class AI:

    def __init__(self, board: Board, depth=3):
        self.board = board
        self.depth = depth
        self.side = 'b'

    def repeated_move(self, piece, i):
        """ Check if last three move are repeated, for dual ai self-play only """
        if self.board.turn_number > 9 and self.board.move_arr[-2][3] == i == self.board.move_arr[-6][3] == \
                self.board.move_arr[-4][4] == self.board.move_arr[-8][4] \
                and self.board.move_arr[-2][5] == self.board.move_arr[-4][5] == piece == self.board.move_arr[-6][5] == \
                self.board.move_arr[-8][5]:
            return True
        return False

    def get_best_move(self, side):
        ...

    def evaluate_board(self, board):
        return sum(
            piece.points + get_position_points(piece)[piece.y][piece.x]
            for piece in board.get_all_pieces()
        )