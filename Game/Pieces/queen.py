from Game.Pieces.bishop import Bishop
from Game.Pieces.piece import Piece
from Game.Pieces.rook import Rook
import GUI.piece_sprites as ps


class Queen(Rook, Bishop, Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.symbol = 'q'
        self.sprite = ps.piece_sprites(self)
        self.points = 90 if self.color == 'w' else -90

    def get_possible_moves(self, board):
        move_arr_rook, capture_arr_rook = self.rook_move(board)
        move_arr_bishop, capture_arr_bishop = self.bishop_move(board)
        move_arr = move_arr_bishop + move_arr_rook
        capture_arr = capture_arr_bishop + capture_arr_rook

        return move_arr, capture_arr
