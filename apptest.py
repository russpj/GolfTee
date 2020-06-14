'''
	apptest.py

	Tests the golf tees game. 
'''

from GolfTees import Rule
from GolfTees import Solve

triangleRules = [
	Rule(0, 1, 3),
	Rule(0, 2, 5),
	Rule(1, 3, 6),
	Rule(1, 4, 8),
	Rule(2, 4, 7),
	Rule(2, 5, 9),
	Rule(3, 1, 0),
	Rule(3, 4, 5),
	Rule(5, 2, 0),
	Rule(5, 4, 3),
	Rule(6, 3, 1),
	Rule(6, 7, 8),
	Rule(7, 4, 2),
	Rule(7, 8, 9),
	Rule(8, 4, 1),
	Rule(8, 7, 6),
	Rule(9, 5, 2),
	Rule(9, 8, 7)
	]

# Start with one blank at the top
board = [False, True, True, True, True, True, True, True, True, True]

def PegChar(peg):
	if peg:
		return 'X'
	else:
		return 'O'

def PrintBoard(board):
	print('   {}'.format(PegChar(board[0])))
	print('  {} {}'.format(PegChar(board[1]), PegChar(board[2])))
	print(' {} {} {}'.format(PegChar(board[3]), PegChar(board[4]), PegChar(board[5])))
	print('{} {} {} {}'.format(PegChar(board[6]), PegChar(board[7]), PegChar(board[8]), PegChar(board[9])))

def Test():
	print ('Running Tests')
	PrintBoard (board)
	for solution in Solve(board, triangleRules, []):
		PrintBoard (board)
	return


if __name__ == '__main__':
	Test()

