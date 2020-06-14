Golf Tees

Golf Tees game solver

Currently Supports console test mode with hard coded boards. 

Necessary Files:
	GolfTees.py
	apptest.py

command line: python apptest.py

This should execute a series of tests, one in verbose mode

I have not verified that this is actually outputting the expected results.

Method:
	This uses a backtracking solver [Solve()] implemented as a python generator

	A jump rule indicates where the peg starts the jump, which hole must have a peg
	to jump over, and which hole must be empty to land in. Each board gets a list of rules
	that apply.

	Currently, the board printing is fixed, so this really only works with one board.
	Note that the printing and rules are defined outside of the solver code.