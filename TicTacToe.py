
from math import inf

class TicTacToe:
    
    def __init__(self):
        self.reset()
        self.human = 1
        self.ai = 2
        self.turn = self.human
        self.scores = {'1': 10, '2': -10, '0': 0}

    def reset(self):
        # Reset the game to the original position
        self.board = [0 for i in range(9)]

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
        # TODO: What is better: Using self.turn? Or player as a variable passed into this func?
        if act < 9 and act >= 0: # TODO: Can I write this nicer?
            if self.board[act] == 0: # TODO: Move into a method 'legal_move()'?
                self.board[act] = player
                return True
            else: 
                # TODO: Move to input validation?
                # if player == 1: print('This is a non-empty field, idiot.')
                return False
        else:
            # if player == 1: print('Impossible move, asshole.')
            return False
    
    def is_winner(self):
        winner = False
        # Check columns, rows and the two diagonals
        for i in range(3):     
            if len(set([self.board[i], self.board[i+3], self.board[i+6]])) == 1 and self.board[i] != 0:
                winner = self.board[i]
        for i in range(0, 7, 3):
            if len(set([self.board[i], self.board[i+1], self.board[i+2]])) == 1 and self.board[i] != 0:
                winner = self.board[i]
        if len(set([self.board[0], self.board[4], self.board[8]])) == 1 and self.board[0] != 0:
            winner = self.board[0]
        if len(set([self.board[2], self.board[4], self.board[6]])) == 1 and self.board[2] != 0:
            winner = self.board[2]

        # Check if tie
        if winner == False and 0 not in self.board:
            return 0
        elif winner != False:
            return winner
        else:
            return None

    def minimax(self, board, maximizing_player=False):
        # Base case
        result = self.is_winner()
        if result != None:
            return self.scores[str(result)]

        # Maximizing player, ai
        if maximizing_player:
            value = -inf
            for i in range(0, 10):
                if self.move(i, self.ai): 
                    value = max(value, self.minimax(self.board, False))
                    self.board[i] = 0      
            return value

        # Minimizing player, human
        else:            
            value = inf
            for i in range(0, 10):
                if self.move(i, self.human):
                    value = min(value, self.minimax(self.board, True))
                    self.board[i] = 0
            return value

    def run(self):
        # Run the game
        self.render_board()
        while True:      
            
            # Human player's turn
            if self.turn == self.human:
                while True:
               
                    # TODO: Handle all kinds of bad input
                    act = int(input('Player {} make your move: '.format(self.turn)))  
                    if self.move(act, self.turn):
                        break
                                    
            # AI's turn (maximizing player)
            else:
                # Find and make best move
                v = -inf
                vacts = []
                for i in range(0, 9):
                    if self.move(i, self.turn):
                        vacts.append((self.minimax(self.board), i))
                        self.board[i] = 0

                print(vacts)
                best_act = max(vacts, key=lambda item:item[0])
                self.move(best_act[1], self.turn)
               
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