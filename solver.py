#!/usr/bin/env python
import numpy as np
import math


# ----------------------------------------- COLUMN SOLVER -----------------------------------------
def column_solver(sudoku, default):
    backup=np.copy(sudoku) # Backing-up the puzzle for comparing in instructions
    for col in range(0,9): # Looping through the columns
        for num in np.setdiff1d(default,sudoku[:,col]): # Loop missing numbers (compare to default)
            for loc in np.argwhere(sudoku[:,col]==0): # Looping through 0 locations in column
                col_3 = int(math.floor(col/3))*3 # Column integer for identifying 3x3 array
                row_3 = int(math.floor(loc/3))*3 # Row integer for identifying 3x3 array
                if num in sudoku[loc,:]: # Rows that contain num
                    continue # Skip if the number is present
                elif num in sudoku[row_3:row_3+3,col_3:col_3+3]: # 3x3 arrays that contain num
                    continue # Skip if the number is present
                else: # Replace the location with a -1
                    sudoku[loc,col] = np.where(sudoku[loc,col]==0, -1, sudoku[loc,col])
            unique, counts = np.unique(sudoku[:,col], return_counts=True) # Count column
            dictionary = dict(zip(unique, counts)) # Dictionary of counted values
            for loc in np.argwhere(sudoku[:,col]==-1): # Looping through the 0's replaced with -1
                if dictionary[-1] == 1: # If there is a single -1
                    # Replace the -1 value with the num
                    sudoku[loc,col] = np.where(sudoku[loc,col]==-1, num, sudoku[loc,col])
                    # Writing instructions
                    f.write("\ncolumn_solver")
                    f.write("\nLocation column-%d/row-%d insert %d\r\n" % (col+1,loc+1,num))
                    np.savetxt(f, sudoku-backup, fmt='%1i') # Graphical instruction
                    backup=np.copy(sudoku) # Replacing the backup with the new puzzle
                    unique, counts = np.unique(sudoku[:,:], return_counts=True) # Count puzzle
                    total = dict(zip(unique, counts)) # Dictionary of counted values
                    if (np.any(sudoku==0))==True: # If there are any 0's in the puzzle
                        f.write("The remaining numbers to be solved: %d\r\n" % (total[0]))
                    else: # If there are no 0's in the puzzle
                        f.write("FINISHED!")
                else: # If more than one 0 has been replaced with a -1 reset back to 0
                    sudoku[loc,col] = np.where(sudoku[loc,col]==-1, 0, sudoku[loc,col])
    return sudoku # Send the updated puzzle back to the main program


# ------------------------------------------- ROW SOLVER ------------------------------------------
def row_solver(sudoku, default):
    backup=np.copy(sudoku) # Backing-up the puzzle for comparing in instructions
    for row in range(0,9): # Looping through the rows
        for num in np.setdiff1d(default,sudoku[row,:]): # Loop missing numbers (compare to default)
            for loc in np.argwhere(sudoku[row,:]==0): # Looping through 0 locations in row
                row_3 = int(math.floor(row/3))*3 # Row integer for identifying 3x3 array
                col_3 = int(math.floor(loc/3))*3 # Column integer for identifying 3x3 array
                if num in sudoku[:,loc]: # Rows that contain num
                    continue # Skip if the number is present
                elif num in sudoku[row_3:row_3+3,col_3:col_3+3]: # 3x3 arrays that contain num
                    continue # Skip if the number is present
                else: # Replace the location with a -1
                    sudoku[row,loc] = np.where(sudoku[row,loc]==0, -1, sudoku[row,loc])
            unique, counts = np.unique(sudoku[row,:], return_counts=True) # Count values in column
            dictionary = dict(zip(unique, counts)) # Dictionary of counted values
            for loc in np.argwhere(sudoku[row,:]==-1): # Looping through the 0's replaced with -1
                if dictionary[-1] == 1: # If there is a single -1
                    # Replace the -1 value with the num
                    sudoku[row,loc] = np.where(sudoku[row,loc]==-1, num, sudoku[row,loc])
                    # Writing instructions
                    f.write("\nrow_solver")
                    f.write("\nLocation row-%d/column-%d insert %d\r\n" % (row+1,loc+1,num))
                    np.savetxt(f, sudoku-backup, fmt='%1i') # Graphical instruction
                    backup=np.copy(sudoku) # Replacing the backup with the new puzzle
                    unique, counts = np.unique(sudoku[:,:], return_counts=True) # Count puzzle
                    total = dict(zip(unique, counts)) # Dictionary of counted values
                    if (np.any(sudoku==0))==True: # If there are any 0's in the puzzle
                        f.write("The remaining numbers to be solved: %d\r\n" % (total[0]))
                    else: # If there are no 0's in the puzzle
                        f.write("FINISHED!")
                else: # If more than one 0 has been replaced with a -1 reset back to 0
                    sudoku[row,loc] = np.where(sudoku[row,loc]==-1, 0, sudoku[row,loc])
    return sudoku # Send the updated puzzle back to the main program


# ---------------------------------------- 3x3 ARRAY SOLVER ---------------------------------------
def array_solver(sudoku, default):
    backup=np.copy(sudoku) # Backing-up the puzzle for comparing in instructions
    for row in range(0,3): # row axis of puzzle
        for col in range(0,3): # column axis of puzzle
            for num in np.setdiff1d(default,sudoku[(row*3):(row*3)+3,(col*3):(col*3)+3]): # Looping through missing numbers (comparing against default)
                for loc in np.argwhere(sudoku[(row*3):(row*3)+3,(col*3):(col*3)+3]==0): # Looping through 0 locations
                    if num in sudoku[row*3+loc[0],:] or num in sudoku[:,col*3+loc[1]]: # Rows and columns that contain num
                        continue # Skip if the number is present
                    else: # If the number is not found
                        sudoku[row*3+loc[0],col*3+loc[1]] = np.where(sudoku[row*3+loc[0],col*3+loc[1]]==0, -1, sudoku[row*3+loc[0],col*3+loc[1]]) # Replace the location with a -1 if not conditions skip it
                unique, counts = np.unique(sudoku[(row*3):(row*3)+3,(col*3):(col*3)+3], return_counts=True) # Count values in 3x3 array
                dictionary = dict(zip(unique, counts)) # Create dictionary of counted values
                for loc in np.argwhere(sudoku[(row*3):(row*3)+3,(col*3):(col*3)+3]==-1): # Looping through the 0's replaced with -1
                    if dictionary[-1] == 1: # If there is a single -1
                        sudoku[row*3+loc[0],col*3+loc[1]] = np.where(sudoku[row*3+loc[0],col*3+loc[1]]==-1, num, sudoku[row*3+loc[0],col*3+loc[1]]) # Replace the -1 with the missing number
                        f.write("\narray_solver")
                        f.write("\nLocation row-%d/column-%d insert %d\r\n" % (loc[1]+1,loc[0]+1,num)) # Writing instructions
                        np.savetxt(f, sudoku-backup, fmt='%1i') # Graphical instruction
                        backup=np.copy(sudoku) # Replacing the backup with the new puzzle
                        unique, counts = np.unique(sudoku[:,:], return_counts=True) # Count values in whole puzzle
                        total = dict(zip(unique, counts)) # Create dictionary of counted values
                        if (np.any(sudoku==0))==True:
                            f.write("The remaining numbers to be solved: %d\r\n" % (total[0]))
                        else:
                            f.write("FINISHED!")
                    elif dictionary[-1] == 2: # If there are two -1's
                        print(dictionary[-1])
                        print(sudoku)
                        print(num)
                        sudoku[row*3+loc[0],col*3+loc[1]] = np.where(sudoku[row*3+loc[0],col*3+loc[1]]==-1, 0, sudoku[row*3+loc[0],col*3+loc[1]]) # Setting the -1 back to 0
                    else: # If more than one 0 has been replaced with a -1
                        sudoku[row*3+loc[0],col*3+loc[1]] = np.where(sudoku[row*3+loc[0],col*3+loc[1]]==-1, 0, sudoku[row*3+loc[0],col*3+loc[1]]) # Setting the -1 back to 0
    return sudoku


# -------------------------------------------MAIN PROGRAM------------------------------------------
if __name__ == '__main__':

    sudoku_in = np.loadtxt("input.txt", dtype="int") # Reading in sudoku puzzle
    sudoku=np.copy(sudoku_in) # Backing up input sudoku to a working array
    f = open("Instructions.txt","w+") # Opening/creating file for outputing instructions
    f.write("Original puzzle:\r\n")
    default = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) # 1D array of sudoku numbers
    np.savetxt(f, sudoku, fmt='%1i') # Saving the puzzle to the instructions
    unique, counts = np.unique(sudoku, return_counts=True) # Count column
    dictionary = dict(zip(unique, counts)) # Create dictionary of counted values
    f.write(str(dictionary))
    f.write("\r\n")


    # Solving the puzzle
    count = 1
    print(sudoku)
    print(" ")
    while (np.any(sudoku==0))==True:
        count += 9
        if count > 20:
            f.close()
            print(count)
            print(sudoku)
            exit()
        column_solver(sudoku, default)
        row_solver(sudoku, default)
        array_solver(sudoku, default)