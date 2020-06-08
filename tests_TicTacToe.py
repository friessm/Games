
import unittest

import TicTacToe

class TicTacToeTest(unittest.TestCase):

    def setUp(self):
        # Intantiate the TicTacToe class
        self.game = TicTacToe.TicTacToe()

    def test_next_turn(self):

        print('Testing next_turn method ... \n')

        # Test if player 1 switches to player 2
        self.game.next_turn()
        self.assertEqual(2, self.game.turn)

        # Test if player 2 switches to player 1
        self.game.next_turn()
        self.assertEqual(1, self.game.turn)


    def test_move(self):      
        
        # TODO: How to supress the text to stdout?
        print('Testing move method ... \n')
        
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
        
        print('Testing is_winner method ... \n')
        
        # Positive cases
        # Test rows and columns for player 1
        tlist1 = [[1, 0, 0, 1, 0, 0, 1, 0, 0],
                  [0, 1, 0, 0, 1, 0, 0, 1, 0],
                  [0, 0, 1, 0, 0, 1, 0, 0, 1],
                  [1, 1, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1, 1, 0, 0, 0],
                  [1, 1, 1, 2, 2, 1, 2, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 1, 1],
                  [2, 2, 0, 1, 1, 1, 0, 0, 0]]

        for i in range(len(tlist1)):
            self.game.board = tlist1[i]
            print(self.game.board)
            self.assertIs(self.game.is_winner(), 1)

        # Test diagonals for player 2
        self.game.next_turn()
        tlist2 = [[2, 0, 0, 0, 2, 0, 0, 0, 2],
                  [0, 0, 2, 0, 2, 0, 2, 0, 0]]

        for i in range(len(tlist2)):
            self.game.board = tlist2[i]
            print(self.game.is_winner())
            self.assertIs(self.game.is_winner(), 2)

        # Negative cases for player 1
        self.game.next_turn()
        tlist3 = [[0, 1, 0, 1, 0, 0, 1, 0, 0],
                  [0, 0, 2, 0, 1, 0, 0, 1, 0],
                  [0, 0, 2, 0, 0, 1, 0, 0, 1],
                  [1, 1, 2, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 2, 1, 0, 0, 0],
                  [1, 1, 0, 2, 2, 1, 2, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 1, 2]]

        for i in range(len(tlist3)):
            self.game.board = tlist3[i]
            self.assertIs(self.game.is_winner(), None)

        # Tie and player 2's turn
        self.game.next_turn()
        tlist4 = [[2, 1, 2, 1, 2, 2, 1, 2, 1],
                  [1, 1, 2, 2, 1, 1, 1, 2, 2]]

        for i in range(len(tlist4)):
            self.game.board = tlist4[i]
            self.assertIs(self.game.is_winner(), 0)


if __name__ == '__main__':
    unittest.main()