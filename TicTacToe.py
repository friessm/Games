
from math import inf

class TicTacToe:
    
    def __init__(self):
        self.reset()
        self.human = 1
        self.ai = 2
        self.turn = self.human
        self.scores = {'1': -10, '2': 10, '0': 0}

    def reset(self):
        """ Reset the game to the original position """
        self.board = [0 for i in range(9)]

    def render_board(self):
        """ Renders board to stdout. """
        for i in range(0, len(self.board), 3):
            print(self.board[i], self.board[i+1], self.board[i+2])
        print('\n')

    def next_turn(self):
        """ Switch who's players turn it is. """
        if self.turn == self.human:
            self.turn = self.ai
        else:
            self.turn = self.human

    def move(self, act, player):
        """ Make valid moves. """
        if self.board[act] == 0:
            self.board[act] = player
            return True
        else: 
            return False

    def valid_moves(self):
        """ Return list of valid moves. """
        return [k for k, v in enumerate(self.board) if v == 0]

    def is_winner(self):
        """ Check columns, rows, the two diagonals and tie, or return None. """
        b = self.board
        for turn in [self.human, self.ai]:
            for i in range(3):     
                if all(x==turn for x in [b[i],b[i+3], b[i+6]]):
                    return turn
                if all(x==turn for x in b[i*3:i*3+3]):
                    return turn
            if all(x==turn for x in [b[0], b[4], b[8]]):
                return turn
            if all(x==turn for x in [b[2], b[4], b[6]]):
                return turn
        if 0 not in b:
            return 0
        return None

    def minimax(self, max_player):
        """ Minimax to find optimal move for ai. """
        res = self.is_winner()
        if res != None:
            return self.scores[str(res)]
        if max_player:
            value = -inf
            for i in self.valid_moves():
                if self.move(i, self.ai):
                    value = max(value, self.minimax(False))
                    self.board[i] = 0
            return value
        else:
            value = inf
            for i in self.valid_moves():
                if self.move(i, self.human):
                    value = min(value, self.minimax(True))
                    self.board[i] = 0
            return value

    def best_ai_act(self):
        """ Initiate search for optimal ai move. """
        vacts = []
        for i in self.valid_moves():
            if self.move(i, self.turn):
                vacts.append((self.minimax(False), i))
                self.board[i] = 0
        best_act = max(vacts, key=lambda item:item[0])
        return best_act[1]

    def get_human_act(self):
        """ Get human player input. """
        while True:
            try:
                act = int(input('Player {} make your move: '.format(self.turn)))
            except ValueError:
                print('Invalid input. Valid input are integers from 0 to 8.')
            if act >= 0 and act < 9:
                if self.board[act] == 0:
                    break
                else:
                    print('This is a non-empty field, idiot.')
            else: 
                print('Invalid input. Valid input are integers from 0 to 8.')
        return act

    def run(self):
        """ Run the game. """ 
        self.render_board()
        while True:      
            if self.turn == self.human:
                while True:
                    if self.move(self.get_human_act(), self.human):
                        break                                 
            else: # AI's turn (maximizing player)
                self.move(self.best_ai_act(), self.turn)

            result = self.is_winner()
            if result != 0 and result != None:
                print('And the winner is: Player {}\n'.format(self.turn))
                self.render_board()
                break

            if result == 0:
                print('Tie. No winner.')
                self.render_board()
                break
        
            self.render_board()
            self.next_turn()


if __name__ == '__main__':
    game = TicTacToe()
    game.run()