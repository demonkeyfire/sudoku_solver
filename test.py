#!/usr/bin/env python
import numpy as np


# Reading in sudoku array
sudoku_in = np.loadtxt("input.txt",dtype="int") # Reading in sudoku text file as numpy array
sudoku = sudoku_in
default = np.array([1,2,3,4,5,6,7,8,9]) # 1D array of sudoku numbers 


# A dictionary of the rows
rows = {}
for i in range(0,9): # cycling through all rows
    rows["row_" + str(i)] = sudoku_in[i,:] # picking up each row

# A dictionary of the columns
columns = {}
for i in range(0,9):
    columns["column_" + str(i)] = sudoku_in[:,i]

# Creating a dictionary of the slices
slices = {}
for i in range(0,3):
    for j in range(0,3):
        slices["slice_"+str(i)+"_"+str(j)] = sudoku_in[j*3:(j*3)+3,i*3:(i*3)+3]


# Finding the 0's in a row
for i in range(0,9):
    if i==0:
        print("This is the row:")
        print(rows["row_"+str(i)])
        print(np.argwhere(rows["row_"+str(i)]==0))

# Finding the 0's in a column
for i in range(0,9):
    if i==0:
        print("This is the column:")
        print(columns["column_"+str(i)])
        print(np.argwhere(columns["column_"+str(i)]==0))

# Finding the 0's in a slice
for i in range(0,9):
    for j in range(0,9):
        if i==0 and j==0:
            print("This is the slice:")
            print(slices["slice_"+str(i)+"_"+str(j)])
            print(np.argwhere(slices["slice_"+str(i)+"_"+str(j)]==0))