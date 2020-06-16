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
	return board[rule.start].filled and board[rule.over].filled and not board[rule.end].filled

def ApplyRule(board, rule):
	board[rule.start].filled = False
	board[rule.over].filled = False
	board[rule.end].filled = True
	return

def UnApplyRule(board, rule):
	board[rule.end].filled = False
	board[rule.over].filled = True
	board[rule.start].filled = True
	return


class Solution(Enum):
	Solved = 1
	NewRule = 2
	BackTrack = 3


def IsBoardWinner(holes):
	return sum(1 for hole in holes if hole.filled) == 1

def Solve(holes, rules, solution):
	if IsBoardWinner(holes):
		yield Solution.Solved

	for rule in rules:
		if (IsRuleValid(holes, rule)):
			ApplyRule(holes, rule)
			solution.append(rule)
			yield Solution.NewRule
			yield from Solve(holes, rules, solution)
			solution.pop()
			UnApplyRule(holes, rule)
			yield Solution.BackTrack
	return


hexDirections = [
		[-1, -1],
		[-1, 1],
		[0, -2],
		[0, 2],
		[1, -1],
		[1, 1]
	]

class Hole:
	def __init__(self, row, col, filled):
		self.row=row
		self.col = col
		self.filled = filled
		return

class HexBoard:
	def __init__(self, locations):
		self.holes = []
		for location in locations:
			if self.IsValidLocation(location):
				self.holes.append(Hole(location[0], location[1], True))
		self.AddRules()
		return

	def IsValidLocation(self, location):
		bothEven = (location[0]%2 == 0 and location[1]%2 == 0)
		bothOdd = (location[0]%2 == 1 and location[1]%2 == 1)
		return bothEven or bothOdd

	def RemovePeg(self, peg):
		self.holes[peg].filled = False

	def FindLocation(self, row, col):
		for index in range(len(self.holes)):
			hole = self.holes[index]
			if hole.row == row and hole.col == col:
				return index
		return -1

	def AddRule(self, start, direction):
		startHole = self.holes[start]
		over = self.FindLocation(startHole.row+direction[0], startHole.col+direction[1])
		if over != -1:
			overHole = self.holes[over]
			end = self.FindLocation(overHole.row+direction[0], overHole.col+direction[1])
			if end != -1:
				self.rules.append(Rule(start, over, end))
		return

	def AddRules(self):
		self.rules = []
		for start in range(len(self.holes)):
			for direction in hexDirections:
				self.AddRule(start, direction)
		return


def CreateTriangleBoard(rows, pegToRemove=-1):
	holes = []
	for row in range(rows):
		firstCol = -row
		for col in range(row+1):
			holes.append([row, firstCol + col*2])
	
			board = HexBoard(holes)
	if pegToRemove != -1:
		board.RemovePeg(pegToRemove)

	return board
			