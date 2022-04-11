from Game.Pieces.piece import Piece

import GUI.piece_sprites as ps


class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.symbol = 'b'
        self.sprite = ps.piece_sprites(self)

        self.points = 30 if self.color == 'w' else -30

    def get_possible_moves(self, board):
        move_arr, capture_arr = self.bishop_move(board)
        return move_arr, capture_arr

    def bishop_move(self, board):
        offsets = ((-1, -1), (1, 1), (1, -1), (-1, 1))
        move_arr, capture_arr = self.generate_moves(board, offsets)
        return move_arr, capture_arr
