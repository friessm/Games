
import unittest

import TicTacToe

class TicTacToeTest(unittest.TestCase):

    def setUp(self):
        # Intantiate the TicTacToe class
        self.game = TicTacToe.TicTacToe()

    def test_move(self):      
        
        # TODO: How to supress the text to stdout?
        print('testing move method ... \n')
        
        # Test the happy cases
        for i in range(0,9):
            self.assertTrue(self.game.move(i, self.game.turn))

        # Test that moves stay inside the board
        for i in range(9, 15):
            self.assertFalse(self.game.move(i, self.game.turn))

        # Test that no move can be overwritten
        self.game.next_turn()
        for i in range(0, 9):
            self.assertFalse(self.game.move(i, self.game.turn))

    def test_is_winner(self):
        
        print('testing is_winner method ... \n')
        
        # Positive cases
        # Test rows and columns for player 1
        tlist1 = [[1, 0, 0, 1, 0, 0, 1, 0, 0],
                  [0, 1, 0, 0, 1, 0, 0, 1, 0],
                  [0, 0, 1, 0, 0, 1, 0, 0, 1],
                  [1, 1, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 1, 1]]

        for i in range(len(tlist1)):
            self.game.board = tlist1[i]
            self.assertTrue(self.game.is_winner())

        # Test diagonals for player 2
        self.game.next_turn()
        tlist2 = [[2, 0, 0, 0, 2, 0, 0, 0, 2],
                  [0, 0, 2, 0, 2, 0, 2, 0, 0]]

        for i in range(len(tlist2)):
            self.game.board = tlist2[i]
            self.assertTrue(self.game.is_winner())

        # Negative cases for player 1
        self.game.next_turn()
        tlist3 = [[0, 1, 0, 1, 0, 0, 1, 0, 0],
                  [0, 0, 2, 0, 1, 0, 0, 1, 0],
                  [0, 0, 2, 0, 0, 1, 0, 0, 1],
                  [1, 1, 2, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 2, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 1, 2]]

        for i in range(len(tlist3)):
            self.game.board = tlist3[i]
            self.assertFalse(self.game.is_winner())


if __name__ == '__main__':
    unittest.main()