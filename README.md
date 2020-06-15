Golf Tees

Golf Tees game solver

Currently Supports console test mode with hard coded boards. 

Necessary Files:
	GolfTees.py
	apptest.py

command line: python apptest.py

I've added a stub for AppMain.py, which will be the main python file for the GUI version.

This should execute a series of tests, one in verbose mode

I believe that this is actually outputting the expected results.

Method:
	This uses a backtracking solver [Solve()] implemented as a python generator

	A jump rule indicates where the peg starts the jump, which hole must have a peg
	to jump over, and which hole must be empty to land in. Each board gets a list of rules
	that apply.

	Currently, the board printing is fixed, so this really only works with one board.
	Note that the printing and rules are defined outside of the solver code.

Notes:
	The only board implemented here is a four row, ten hole board. The 5 row, 15-hole board
	is more common, especially at Cracker Barrel restaurants. I should add that possibility 
	sometime.