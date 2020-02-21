#!/usr/bin/env python
import numpy as np


# sudoku = np.array([[1,2,3],[4,0,6],[7,8,9]]) # Creating a 3x3 array using numpy
sudoku = np.array([1,2,0,4,5,6,7,8,9])
array1 = np.sum(sudoku) # Summing the array for total value


default = np.array([1,2,3,4,5,6,7,8,9]) # A complete list of numbers in 1D array
check = np.isin(sudoku,default) # Checks sudoku[] against default[] and gives true/false array
check2 = np.sum(check)


if check2 == 8:
    sum1 = 45 - np.sum(sudoku)
    check3 = np.argwhere(check==0)
    sudoku1 = np.where(sudoku==0, sum1, sudoku) 


print(sudoku)
print(check)
print(check3)
print(sudoku1)