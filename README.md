Golf Tees

Golf Tees game solver

Currently Supports console test mode with hard coded boards. 

Necessary Files:
	GolfTees.py
	apptest.py

command line: python apptest.py

I've added a stub for AppMain.py, which will be the main python file for the GUI version.

This should execute a series of tests

I believe that this is actually outputting the expected results.

Method:
	This uses a backtracking solver [Solve()] implemented as a python generator.

	A jump rule indicates where the peg starts the jump, which hole must have a peg
	to jump over, and which hole must be empty to land in. Each board gets a list of rules
	that apply.

	The game assumes a hexagonal grid, which is correct for Chinese Checkers and 
	triangular puzzles. There is a method that creates a triangular board of any size,
	CreateTriangleBoard() and the test program is testing 10 hole and 15 hole boards.

Notes:
	The 5 row, 15-hole board is common, especially at Cracker Barrel restaurants. 