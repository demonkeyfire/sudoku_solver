#!/usr/bin/env python
import numpy as np
import math


# ----------------------------------------- COLUMN SOLVER -----------------------------------------
def column_solver(sudoku, default):
    backup=np.copy(sudoku) # Backing-up the puzzle for comparing in instructions
    for i in range(0,9): # Looping through the columns
        for j in np.setdiff1d(default,sudoku[:,i]): # Looping through missing numbers (comparing against default)
            for k in np.argwhere(sudoku[:,i]==0): # Looping through 0 locations in column
                m = int(math.floor(i/3))*3 # Column integer for identifying 3x3 array
                n = int(math.floor(k/3))*3 # Row integer for identifying 3x3 array
                if j in sudoku[k,:]: # Rows that have the number j
                    continue # Skip if the number is present
                elif j in sudoku[n:n+3,m:m+3]: # 3x3 arrays that have the number j
                    continue # Skip if the number is present
                else: # If the number is not found
                    sudoku[k,i] = np.where(sudoku[k,i]==0, -1, sudoku[k,i]) # Replace the location with a -1 if not conditions skip it
            unique, counts = np.unique(sudoku[:,i], return_counts=True) # Count values in column
            dictionary = dict(zip(unique, counts)) # Create dictionary of counted values
            for k in np.argwhere(sudoku[:,i]==-1): # Looping through the 0's replaced with -1
                if dictionary[-1] == 1: # If there is a single -1
                    sudoku[k,i] = np.where(sudoku[k,i]==-1, j, sudoku[k,i]) # Replace the -1 with the missing number
                    f.write("\nLocation column-%d/row-%d insert %d\r\n" % (i+1,k+1,j)) # Writing instructions
                    np.savetxt(f, sudoku-backup, fmt='%1i') # Graphical instruction
                    backup=np.copy(sudoku) # Replacing the backup with the new puzzle
                    unique, counts = np.unique(sudoku[:,:], return_counts=True) # Count values in whole puzzle
                    total = dict(zip(unique, counts)) # Create dictionary of counted values
                    if (np.any(sudoku==0))==True:
                        f.write("The remaining numbers to be solved: %d\r\n" % (total[0]))
                    else:
                        f.write("FINISHED!")
                else: # If more than one 0 has been replaced with a -1
                    sudoku[k,i] = np.where(sudoku[k,i]==-1, 0, sudoku[k,i]) # Setting the -1 back to 0
    return sudoku


# ------------------------------------------- ROW SOLVER ------------------------------------------
def row_solver(sudoku, default):
    backup=np.copy(sudoku) # Backing-up the puzzle for comparing in instructions
    for i in range(0,9): # Looping through the rows
        for j in np.setdiff1d(default,sudoku[i,:]): # Looping through missing numbers (comparing against default)
            for k in np.argwhere(sudoku[i,:]==0): # Looping through 0 locations in row
                m = int(math.floor(i/3))*3 # Row integer for identifying 3x3 array
                n = int(math.floor(k/3))*3 # Column integer for identifying 3x3 array
                if j in sudoku[:,k]: # Rows that have the number j
                    continue # Skip if the number is present
                elif j in sudoku[m:m+3,n:n+3]: # 3x3 arrays that have the number j
                    continue # Skip if the number is present
                else: # If the number is not found
                    sudoku[i,k] = np.where(sudoku[i,k]==0, -1, sudoku[i,k]) # Replace the location with a -1 if not conditions skip it
            unique, counts = np.unique(sudoku[i,:], return_counts=True) # Count values in column
            dictionary = dict(zip(unique, counts)) # Create dictionary of counted values
            for k in np.argwhere(sudoku[i,:]==-1): # Looping through the 0's replaced with -1
                if dictionary[-1] == 1: # If there is a single -1
                    sudoku[i,k] = np.where(sudoku[i,k]==-1, j, sudoku[i,k]) # Replace the -1 with the missing number
                    f.write("\nLocation row-%d/column-%d insert %d\r\n" % (i+1,k+1,j)) # Writing instructions
                    np.savetxt(f, sudoku-backup, fmt='%1i') # Graphical instruction
                    backup=np.copy(sudoku) # Replacing the backup with the new puzzle
                    unique, counts = np.unique(sudoku[:,:], return_counts=True) # Count values in whole puzzle
                    total = dict(zip(unique, counts)) # Create dictionary of counted values
                    if (np.any(sudoku==0))==True:
                        f.write("The remaining numbers to be solved: %d\r\n" % (total[0]))
                    else:
                        f.write("FINISHED!")
                    # print(sudoku-backup)
                    # print(sudoku)
                else: # If more than one 0 has been replaced with a -1
                    sudoku[i,k] = np.where(sudoku[i,k]==-1, 0, sudoku[i,k]) # Setting the -1 back to 0


# -------------------------------------------MAIN PROGRAM------------------------------------------
if __name__ == '__main__':

    sudoku_in = np.loadtxt("input.txt", dtype="int") # Reading in sudoku puzzle
    sudoku=np.copy(sudoku_in) # Backing up input sudoku to a working array
    f = open("Instructions.txt","w+") # Opening/creating file for outputing instructions
    f.write("Original puzzle:\r\n")
    default = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) # 1D array of sudoku numbers
    np.savetxt(f, sudoku, fmt='%1i') # Saving the puzzle to the instructions

    # Solving the puzzle
    count = 1
    while (np.any(sudoku==0))==True:
        count += 1
        if count > 10:
            exit()
        column_solver(sudoku, default)
        row_solver(sudoku, default)
        print(sudoku)
    f.close()