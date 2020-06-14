''' 
	golftees.py

	Implements the algorithm for solving the golf tees puzzle
'''

'''
	This is the classic triangular board
										0
									1   2
							  3   4   5
							6   7   8   9
'''

class Rule:
	def __init__(self, start, over, end):
		self.start = start
		self.over = over
		self.end = end
		return

def IsRuleValid(board, rule):
	return board[rule.start] and board[rule.over] and not board[rule.end]

def IsBoardWinner(board):
	count = 0
	for hole in board:
		if hole:
			count += 1
	return count == 1


def ApplyRule(board, rule):
	board[rule.start] = False
	board[rule.over] = False
	board[rule.end] = True
	return

def UnapplyRule(board, rule):
	board[rule.end] = False
	board[rule.over] = True
	board[rule.start] = True
	return

def Solve(board, rules, solution):
	if IsBoardWinner(board):
		yield solution

	for rule in rules:
		if (IsRuleValid(board, rule)):
			ApplyRule(board, rule)
			solution.append(rule)
			yield solution
			yield from Solve(board, rules, solution)
			solution.pop()
			UnapplyRule(board, rule)
