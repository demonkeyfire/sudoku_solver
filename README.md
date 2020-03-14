# sudoku_solver

## Introduction

A python script that will take in a text file with an unsolved sudoku puzzle and output the instructions of how to solve the sudoku with images of the completed sudokus.

## Working document

A python file 'test.py' will be used to test solution ideas. (removed)
  --> Moved away from having separate working and testing filies and instead working with git branches

The input file is called 'input.txt' and holds the unsolved sudoku puzzle.

The main file for deciding where to put new numbers in the puzzle is 'solver.py'. The reading in of the sudoku puzzle and outputting of the finished product and instructions will be separated out into different files. Looking to understand and use pythong library file structure with a simple front script that will call the solver, input and output libraries.

How the program solves a sudoku puzzle:

1.  def single_number: A row, column or 3x3 array that has a single missing number can solved, i.e. finding the last number, using the function 'single_number()'. Initially the function checks to see if the whole array has been solved. The function checks in all rows, columns and slices (in that order) whether there is more than one missing number (a 0) and if there is only a single missing value will calculate what the missing number is and fill the missing value with that calculated number.

2. def double_number(): 

## Output

A text file that shows the sudoku puzzle as it is solved number by number and the instructions for each number.

## Final Product

The idea is to have a quick script which the numbers from a Sudoku board can be input and will be able to solve in stages and display the changes.