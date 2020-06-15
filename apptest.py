'''
	apptest.py

	Tests the golf tees game. 
'''

from GolfTees import Rule
from GolfTees import Solve
from GolfTees import Solution

'''
	This is the classic 10-hole triangular board
										0
									1   2
							  3   4   5
							6   7   8   9
'''

triangleRules10 = [
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

triangleBoards10 = [
	# one blank at the top
	[False, True, True, True, True, True, True, True, True, True],
	# one blank on the side
	[True, False, True, True, True, True, True, True, True, True],
	# one blank in the middle
	[True, True, True, True, False, True, True, True, True, True]
	]

cases10 = (triangleRules10, triangleBoards10)

def PegChar(peg):
	if peg:
		return 'X'
	else:
		return 'O'

def PrintRowForTriange(board, start, end):
	
	return

def PrintBoard(board):
	print('   {}'.format(PegChar(board[0])))
	print('  {} {}'.format(PegChar(board[1]), PegChar(board[2])))
	print(' {} {} {}'.format(PegChar(board[3]), PegChar(board[4]), PegChar(board[5])))
	print('{} {} {} {}'.format(PegChar(board[6]), PegChar(board[7]), PegChar(board[8]), PegChar(board[9])))
	return

def PrintSolution(solution):
	for rule in solution:
		print ('{} jumps over {} to  {}'.format(rule.start, rule.over, rule.end))

def TestBoard(board, rules, diagnose=False):
	print ('Running Test')
	PrintBoard (board)
	solution = []
	for result in Solve(board, rules, solution):
		if result == Solution.Solved or diagnose:
			print ('{} at level {}'.format(result, len(solution)))
			PrintSolution(solution)
			PrintBoard (board)
	return


def TestCases(rules, boards, diagnose=False):
	for board in boards:
		TestBoard(board, rules, diagnose)
	return

def Test():
	print ('Running Tests')
	TestCases(cases10[0], cases10[1])
	return

if __name__ == '__main__':
	Test()

