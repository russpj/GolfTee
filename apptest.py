'''
	apptest.py

	Tests the golf tees game. 
'''

from GolfTees import Rule
from GolfTees import Solve
from GolfTees import Solution
from GolfTees import CreateTriangleBoard

'''
	This is the classic 10-hole triangular board
										0
									1   2
							  3   4   5
							6   7   8   9
'''


def PegChar(peg):
	if peg:
		return 'X'
	else:
		return 'O'

def PrintHexBoard(board):
	rowStrings = []
	pumpNeedsPriming = True
	currentRow = 0
	minCol = 100000000
	for hole in board.holes:
		if pumpNeedsPriming or hole.row != currentRow:
			rowStrings.append([hole])
			currentRow = hole.row
			firstCol = hole.col
			if firstCol < minCol:
				minCol = firstCol
			pumpNeedsPriming = False
		else:
			rowStrings[-1].append(hole)
	for rowString in rowStrings:
		colDiff = rowString[0].col - minCol
		for space in range(colDiff):
			print(' ', end='')
		for hole in rowString:
			print ('{} '.format(PegChar(hole.filled)), end='')
		print()
	return

def PrintSolution(solution):
	for rule in solution:
		print ('{} jumps over {} to  {}'.format(rule.start, rule.over, rule.end))

def TestBoard(board, diagnose=False):
	print ('Running Test')
	PrintHexBoard (board)
	solution = []
	for result in Solve(board.holes, board.rules, solution):
		if result == Solution.Solved or diagnose:
			print ('{} at level {}'.format(result, len(solution)))
			PrintSolution(solution)
			PrintHexBoard (board)
	return


def Test():
	print ('Running Tests')

	testBoards = []
	testBoards.append(CreateTriangleBoard(4, 0))
	testBoards.append(CreateTriangleBoard(4, 1))
	testBoards.append(CreateTriangleBoard(4, 4))
	testBoards.append(CreateTriangleBoard(5, 4))

	for board in testBoards:
		TestBoard(board)

	return

if __name__ == '__main__':
	Test()

