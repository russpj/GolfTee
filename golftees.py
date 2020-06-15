''' 
	golftees.py

	Implements the algorithm for solving the golf tees puzzle
'''

from enum import Enum


class Rule:
	def __init__(self, start, over, end):
		self.start = start
		self.over = over
		self.end = end
		return

def IsRuleValid(board, rule):
	return board[rule.start] and board[rule.over] and not board[rule.end]

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


class Solution(Enum):
	Solved = 1
	NewRule = 2
	BackTrack = 3

def IsBoardWinner(board):
	count = 0
	for hole in board:
		if hole:
			count += 1
	return count == 1


def Solve(board, rules, solution):
	if IsBoardWinner(board):
		yield Solution.Solved

	for rule in rules:
		if (IsRuleValid(board, rule)):
			ApplyRule(board, rule)
			solution.append(rule)
			yield Solution.NewRule
			yield from Solve(board, rules, solution)
			solution.pop()
			UnapplyRule(board, rule)
			yield Solution.BackTrack
	return


class HexBoard:
	def __init__(self, holes):
		self.holes = []
		for hole in holes:
			if self.IsValidHole(hole):
				self.holes.append(hole)
		return

	def IsValidHole(self, hole):
		bothEven = (hole[0]%2 == 0 and hole[1]%2 == 0)
		bothOdd = (hole[0]%2 == 1 and hole[1]%2 == 1)
		return bothEven or bothOdd


def CreateTriangleBoard(rows):
	holes = []
	for row in range(rows):
		firstCol = -row
		for col in range(row+1):
			holes.append([row, firstCol + col*2])
	return HexBoard(holes)
			