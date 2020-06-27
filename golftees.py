''' 
	golftees.py

	Implements the algorithm for solving the golf tees puzzle
'''

from enum import Enum


class Rule:
	"""
	A Rule is a triple of an allowed jump
	"""
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
	"""
	We're going to have a generator that yields intermediate results.
	"""
	Solved = 1
	NewRule = 2
	BackTrack = 3


def IsBoardWinner(holes):
	return sum(1 for hole in holes if hole.filled) == 1

def Solve(holes, rules, solution):
	"""
	The generator that solves a puzzle

	It will find every solution, and yield intermediate results
	so that the client can update the progress of the solving.
	"""
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
	"""
	This board represents a hexagonal grid, and knows how
	holes line up on the grid.

	It uses a staggered numbering scheme. Even rows only have the even numbered
	columns. Odd rows only odd columns.

	The main data struct is the list of holes. The game sets up which locations on 
	the grid are holes for the game.

	The initializer takes a list of co-ordinates, validates them, and sets them up
	on the board as filled.
	"""
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
	"""
	This creates a triangle on a hex board with the required number of rows.

	The classic game had five rows.
	"""
	holes = []
	for row in range(rows):
		firstCol = -row
		for col in range(row+1):
			holes.append([row, firstCol + col*2])
	
			board = HexBoard(holes)
	if pegToRemove != -1:
		board.RemovePeg(pegToRemove)

	return board
			