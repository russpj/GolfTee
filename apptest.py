'''
	apptest.py

	Tests the golf tees game. 
'''

from GolfTees import Rule
from GolfTees import Solve
from GolfTees import Solution

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

# one blank at the top
board1 = [False, True, True, True, True, True, True, True, True, True]
# one blank on the side
board2 = [True, False, True, True, True, True, True, True, True, True]
# one blank in the middle
board3 = [True, True, True, True, False, True, True, True, True, True]

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
	return

def PrintSolution(solution):
	for rule in solution:
		print ('{} jumps over {} to  {}'.format(rule.start, rule.over, rule.end))

def TestBoard(board, diagnose=False):
	print ('Running Test')
	PrintBoard (board)
	solution = []
	for result in Solve(board, triangleRules, solution):
		if result == Solution.Solved or diagnose:
			print (result)
			PrintSolution(solution)
			PrintBoard (board)
	return


def Test():
	print ('Running Tests')
	TestBoard(board1, True)
	TestBoard(board2)
	TestBoard(board3)
	return

if __name__ == '__main__':
	Test()

