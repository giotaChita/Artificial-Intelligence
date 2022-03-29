
# x wins = +1 , maximizing player
# o wins = -1, minimizing player
# tie = 0


class TicTacToe:
    def __init__(self):
        self.init_game()
        self.board = []
        self.rows = 3
        self.columns = 3
        self.max_player, self.min_player = 'x', 'o'


    def create_board(self):
        for i in range(self.rows):
            self.board.append(['_' for _ in range(self.columns)])
        return self.board

    def stop_condition(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] != '_':
                    return True
        return False


    def static_evaluation():

        return True



    def find_bestM_move(self):
        best_move = None
        for child in self.board:
            if self.minimax(child) > best_move:
                best_move = self.minimax(child)


    # check if there are any moves left on board
    def available_move(self,board):
        for i in range(self.rows):
            for j in range(self.columns):
                if board[i][j] == '_':
                    return True
        return False

    def evaluation(self,board):

        for row in range(self.rows):
            if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
               if board[row][0] == self.max_player:
                   return 1
               elif board[row][0] == self.min_player:
                   return -1
        for col in range(self.rows):
            if board[0][col] == board[1][col] and board[1][col] == board[2][col]
                if board[0][col] == self.max_player:
                    return 1
                elif board[0][col] == self.min_player:
                    return -1
        if board[0][0] == board[1][1] and board[1][1] = board[2][2]:
            if board[0][0] == self.max_player:
                return 1
            elif board[0][0] == self.min_player:
                return -1
        if board[0][2] == board[1][2] and board[1][2] == board[2][0]:
            if board[0][0] == self.max_player:
                return 1
            elif board[0][0] == self.min_player:
                return -1
        # if we have a tie :
        return 0


    def minimax(self,position,depth, alpha, beta, max_player):
        if depth == 0:
            return self.evaluation(position)

        if max_player:
            max_eval = float('-inf')
            for child in position:
                eval = self.minimax(self,child, depth-1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                beta = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for child in position:
                eval = self.minimax(self,child, depth-1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, min_eval)
                if beta <= alpha:
                    break
            return min_eval



