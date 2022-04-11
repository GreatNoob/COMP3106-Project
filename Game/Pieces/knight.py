from Game.Pieces.piece import Piece, is_on_board
import GUI.piece_sprites as ps


class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.symbol = 'n'
        self.sprite = ps.piece_sprites(self)
        self.points = 30 if self.color == 'w' else -30

    def get_possible_moves(self, board):
        move_arr = []
        capture_arr = []

        for i in (-2, -1, 1, 2):
            for j in (-2, -1, 1, 2):
                new_x = self.x + i
                new_y = self.y + j
                if abs(i) != abs(j) and is_on_board(new_x, new_y):
                    if board.board_arr[new_x][new_y] is None:
                        move_arr.append([new_x, new_y])
                    else:
                        if board.board_arr[new_x][new_y].color != self.color:
                            capture_arr.append([new_x, new_y])

        return move_arr, capture_arr

