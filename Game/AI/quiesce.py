from Game.Board.board import Board
from Game.AI.ai import AI
from Game.utils import flip_color

def z_g(n):
    if n <= 0:
        return 0
    return n

class AIQuiesce(AI):
    INF = 99999

    def __init__(self, board: Board, depth=3):
        super().__init__(board, depth)

    def get_best_move(self, side):
        self.side = side

        best_move_eval = -AIQuiesce.INF
        best_move = None
        piece_to_move = None

        alpha = -(AIQuiesce.INF + 1)
        beta = AIQuiesce.INF + 1
        
        for board, piece, move in self.board.get_all_legal_board_states(self.side):
            if self.repeated_move(piece, move):
                continue
            evaluation = -self.minmax_ab(self.depth-1, board, -beta, -alpha, flip_color(self.side))
            if evaluation > best_move_eval:
                best_move = move
                piece_to_move = piece
                best_move_eval = evaluation

            alpha = max(evaluation, alpha)
        
        return piece_to_move, best_move

    def minmax_ab(self, depth, board: Board, alpha, beta, color):
        best_move_eval = -AIQuiesce.INF
        if depth == 0:
            return self.quiesce(board, alpha, beta, color)

        for board_, _, _ in board.get_all_legal_board_states(color):
            score = -self.minmax_ab(depth-1, board_, -beta, -alpha, flip_color(color))

            if score >= beta:
                return score
            
            best_move_eval = max(best_move_eval, score)
            alpha = max(alpha, score)

        return best_move_eval

    
    def quiesce(self, board: Board, alpha, beta, color):
        evaluation = self.evaluate_board2(board, color)
        if evaluation >= beta:
            return beta
        alpha = max(alpha, evaluation)

        for board_, _, _ in board.get_all_legal_board_states_from_capture_moves(color):
            score = -self.quiesce(board_, -beta, -alpha, flip_color(color))

            if score >= beta:
                return beta
            alpha = max(alpha, score)

        return alpha

    def evaluate_board2(self, board, color):
        value = self.evaluate_board(board)
        return value if color == self.side else -value