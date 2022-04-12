from Game.Board.board import Board
from Game.AI.ai import AI
from Game.utils import flip_color

class AIAlphaBeta(AI):
    INF = 99999

    def __init__(self, board: Board, depth=3):
        super().__init__(board, depth)

    def get_best_move(self, side):
        self.side = side

        best_move_eval = -AIAlphaBeta.INF
        best_move = None
        piece_to_move = None
        
        for board, piece, move in self.board.get_all_legal_board_states(self.side):
            if self.repeated_move(piece, move):
                continue
            evaluation = self.minmax(self.depth-1, board, -(AIAlphaBeta.INF+1), AIAlphaBeta.INF+1, False)
            if evaluation >= best_move_eval:
                best_move = move
                piece_to_move = piece
                best_move_eval = evaluation
        
        print(f"evaluation: {evaluation}")
        return piece_to_move, best_move

    def minmax(self, depth, board: Board, alpha, beta, is_maximizing_player: bool):
        if depth == 0:
            return -self.evaluate_board(board)

        if is_maximizing_player:
            best_move_eval = -AIAlphaBeta.INF
            for board_, _, _ in board.get_all_legal_board_states(self.side):
                best_move_eval = max(
                    best_move_eval, 
                    self.minmax(depth-1, board_, alpha, beta, not is_maximizing_player)
                )
                alpha = max(best_move_eval, alpha)
                if alpha >= beta:
                    return best_move_eval
            return best_move_eval
        else:
            worst_move_eval = AIAlphaBeta.INF
            for board_, _, _ in board.get_all_legal_board_states(flip_color(self.side)):
                worst_move_eval = min(
                    worst_move_eval, 
                    self.minmax(depth-1, board_, alpha, beta, not is_maximizing_player)
                )
                beta = min(worst_move_eval, beta)
                if alpha >= beta:
                    return worst_move_eval
            return worst_move_eval