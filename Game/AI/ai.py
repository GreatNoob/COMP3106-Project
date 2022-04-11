from Game.Board.board import Board
from Game.AI.position_points import get_position_points

class AI:
    INF = 99999

    def __init__(self, board: Board, side, depth=3):
        self.board = board
        self.depth = depth
        self.side = side

    def get_best_move(self):
        best_move_eval = -AI.INF
        best_move = None
        piece_to_move = None
        
        for board, piece, move in self.board.get_all_legal_board_states(self.side):
            evaluation = self.minmax(self.depth-1, board, -(AI.INF+1), AI.INF+1, False)
            if evaluation >= best_move_eval:
                best_move = move
                piece_to_move = piece
                best_move_eval = evaluation
        
        return piece_to_move, best_move

    def minmax(self, depth, board: Board, alpha, beta, is_maximizing_player: bool):
        if depth == 0:
            return -self.evaluate_board(board)

        if is_maximizing_player:
            best_move_eval = -AI.INF
            for board_, _, _ in board.get_all_legal_board_states("b"):
                best_move_eval = max(
                    best_move_eval, 
                    self.minmax(depth-1, board_, alpha, beta, not is_maximizing_player)
                )
                alpha = max(best_move_eval, alpha)
                if alpha >= beta:
                    return best_move_eval
            return best_move_eval
        else:
            worst_move_eval = AI.INF
            for board_, _, _ in board.get_all_legal_board_states("w"):
                worst_move_eval = min(
                    worst_move_eval, 
                    self.minmax(depth-1, board_, alpha, beta, not is_maximizing_player)
                )
                beta = min(worst_move_eval, beta)
                if alpha >= beta:
                    return worst_move_eval
            return worst_move_eval

    def evaluate_board(self, board):
        return sum(
            piece.points + get_position_points(piece)[piece.y][piece.x]
            for piece in board.get_all_pieces()
        )