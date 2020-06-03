
import unittest

import TicTacToe

class TicTacToeTest(unittest.TestCase):

    def setUp(self):
        # Intantiate the TicTacToe class
        self.game = TicTacToe.TicTacToe()

    def test_move(self):      
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

        t1 = [1, 0, 0, 1, 0, 0, 1, 0, 0]
        




if __name__ == '__main__':
    unittest.main()