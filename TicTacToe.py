
class TicTacToe:
    
    def __init__(self):
        self.reset()
        self.player1 = 1
        self.player2 = 2
        self.turn = self.player1

    def reset(self):
        # Reset the game to the original position
        self.board = [0 for i in range(9)]

    def render_board(self):
        for i in range(0, len(self.board), 3):
            print(self.board[i], self.board[i+1], self.board[i+2])
        print('\n')

    def next_turn(self):
        # Switch who's players turn it is.
        if self.turn == self.player1:
            self.turn = self.player2
        else:
            self.turn = self.player1

    def move(self, act, player):
        # TODO: What is better: Using self.turn? Or player as a variable passed into this func?
        if act < 9 and act >= 0: # TODO: Can I write this nicer?
            if self.board[act] == 0: # TODO: Move into a method 'legal_move()'?
                self.board[act] = player
                return True
            else: 
                print('This is a non-empty field, idiot.')
                return False
        else:
            print('Impossible move, asshole.')
            return False
    
    def is_winner(self):
        # TODO: What is better: Using self.board? Or board as a variable passed into this func?
        # TODO: Write a test case for this method.
        # Determine that there is a winner and return who won. Else, return false.
        
        # Check rows and columns
        for i in range(3):     
            if all([j == self.turn for j in [self.board[i], self.board[i+3], self.board[i+6]]]):
                return True
        for i in range(0, 7, 3):
            if all([j == self.turn for j in [self.board[i], self.board[i+1], self.board[i+2]]]):
                return True
        
        # Check the two diagonals
        if all([j == self.turn for j in [self.board[0], self.board[4], self.board[8]]]):
            return True
        if all([j == self.turn for j in [self.board[2], self.board[4], self.board[6]]]):
            return True

        # No winner, yet.
        else:
            return False

    def minimax(self):
        pass

    def run(self):
        # Run the game
        self.render_board()
        while True:      
            while True:
                # TODO: Handle all kinds of bad input
                act = int(input('Player {} make your move: '.format(self.turn)))  
                if self.move(act, self.turn):
                    break
            
            if self.is_winner():
                print('And the winner is: Player {}'.format(self.turn))
                self.render_board()
                break
            
            self.render_board()
            self.next_turn()


if __name__ == '__main__':
    game = TicTacToe()
    game.run()