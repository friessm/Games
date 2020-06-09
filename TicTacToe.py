
from math import inf

class TicTacToe:
    
    def __init__(self):
        self.reset()
        self.human = 1
        self.ai = 2
        self.turn = self.ai
        self.scores = {'1': -10, '2': 10, '0': 0}

    def reset(self):
        # Reset the game to the original position
        # self.board = [0 for i in range(9)]
        self.board = [2, 1, 2, 1, 1, 0, 1, 2, 0]

    def render_board(self):
        for i in range(0, len(self.board), 3):
            print(self.board[i], self.board[i+1], self.board[i+2])
        print('\n')

    def next_turn(self):
        # Switch who's players turn it is.
        if self.turn == self.human:
            self.turn = self.ai
        else:
            self.turn = self.human

    def move(self, act, player):
        if self.board[act] == 0:
            self.board[act] = player
            return True
        else: 
            # if player == 1: print('This is a non-empty field, idiot.')
            return False

    def is_winner(self):
        """ Check columns, rows, the two diagonals and tie, or return None. """
        for i in range(3):     
            if all(x==self.turn for x in [self.board[i], self.board[i+3], self.board[i+6]]):
                return self.turn
            if all(x==self.turn for x in self.board[i*3:i*3+3]):
                return self.turn
        if all(x==self.turn for x in [self.board[0], self.board[4], self.board[8]]):
            return self.turn
        if all(x==self.turn for x in [self.board[2], self.board[4], self.board[6]]):
            return self.turn
        if 0 not in self.board:
            return 0
        else:
            return None

    def minimax(self, maximizing_player):
        res = self.is_winner()
        if res != None:
            return self.scores[str(res)]
        self.next_turn()
        if maximizing_player:
            value = -inf
            for i in range(0, 9):
                if self.move(i, self.turn):
                    value = max(value, self.minimax(False))
                    self.board[i] = 0
            return value
        else:
            value = inf
            for i in range(0, 9):
                if self.move(i, self.turn):
                    value = min(value, self.minimax(True))
                    self.board[i] = 0
            return value

    def best_ai_move(self):
        vacts = []
        for i in range(0, 9):
            if self.move(i, self.ai):
                vacts.append((self.minimax(False), i))
                self.board[i] = 0
                self.next_turn()
        best_act = max(vacts, key=lambda item:item[0])
        if self.turn == self.human:
            self.next_turn()
        return best_act[1]

    def run(self):
        # Run the game
        self.render_board()
        while True:      
            print('Next turn: {}'.format(self.turn))
            if self.turn == self.human:
                while True:
                    # TODO: Handle all kinds of bad input
                    act = int(input('Player {} make your move: '.format(self.turn)))  
                    if self.move(act, self.human):
                        break                                 
            # AI's turn (maximizing player)
            else:
                self.move(self.best_ai_move(), self.turn)

            result = self.is_winner()
            if result != 0 and result != None:
                print('And the winner is: Player {}'.format(self.turn))
                self.render_board()
                break
        
            self.render_board()
            self.next_turn()


if __name__ == '__main__':
    game = TicTacToe()
    game.run()