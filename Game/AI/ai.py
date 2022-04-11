from Game.Board.board import Board
from Game.AI.position_points import get_position_points

def flip_color(color):
    return 'w' if color == 'b' else 'b'

class AI:
    INF = 99999

    def __init__(self, board: Board, depth=3):
        self.board = board
        self.depth = depth
        self.side = 'b'

    def get_best_move(self, side):
        self.side = side

        best_move_eval = -AI.INF
        best_move = None
        piece_to_move = None
        
        for board, piece, move in self.board.get_all_legal_board_states(self.side):
            if self.repeated_move(piece, move):
                continue
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
            worst_move_eval = AI.INF
            for board_, _, _ in board.get_all_legal_board_states(flip_color(self.side)):
                worst_move_eval = min(
                    worst_move_eval, 
                    self.minmax(depth-1, board_, alpha, beta, not is_maximizing_player)
                )
                beta = min(worst_move_eval, beta)
                if alpha >= beta:
                    return worst_move_eval
            return worst_move_eval

#### MINMAXROOT ####
    def minmaxRoot(self, depth, board: Board, is_maximizing_player: bool):

        newGameMoves = board.ugly_moves()
        bestMove = -9999
        bestMoveFound = []

        for i in range(0, len(newGameMoves)):
            newGameMove = newGameMoves[i]
            board.ugly_move(newGameMove)
            value = self.minmax(depth-1, board, -10000, 10000, not is_maximizing_player)
            board.undo()

            if(value >= bestMove):
                bestMove = value
                bestMoveFound = newGameMove

        return bestMoveFound
#####################

    def get_best_move2(self, side):
        self.side = side

        best_move_eval = -AI.INF
        best_move = None
        piece_to_move = None

        alpha = -(AI.INF + 1)
        beta = AI.INF + 1
        
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
        best_move_eval = -AI.INF
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

    def evaluate_board(self, board):
        return sum(
            piece.points + get_position_points(piece)[piece.y][piece.x]
            for piece in board.get_all_pieces()
        )

    def repeated_move(self, piece, i):
        """ Check if last three move are repeated, for dual ai self-play only """
        if self.board.turn_number > 9 and self.board.move_arr[-2][3] == i == self.board.move_arr[-6][3] == \
                self.board.move_arr[-4][4] == self.board.move_arr[-8][4] \
                and self.board.move_arr[-2][5] == self.board.move_arr[-4][5] == piece == self.board.move_arr[-6][5] == \
                self.board.move_arr[-8][5]:
            return True
        return False