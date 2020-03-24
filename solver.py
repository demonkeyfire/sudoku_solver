#!/usr/bin/env python
import numpy as np
import math


# --------------------------------SOLVING FOR A SINGLE MISSING VALUE-------------------------------
'''def single_number(sudoku, default, mode):
    # Searching rows for single missing values
    if mode==0:
        for i in range(0,9):
            if (np.sum(np.isin(sudoku[i,:],default))) == 8: # checking if a single value is missing
                print("The initial row "+str(i+1)+":")
                print(sudoku[i,:])
                number = 45 - np.sum(sudoku[i,:]) # calculating missing value
                location = np.argwhere(sudoku[i,:]==0) # location of missing value
                sudoku[i,:] = np.where(sudoku[i,:]==0, number, sudoku[i,:]) # replacing missing value
                print("\nThe missing value at location "+str(np.asscalar(location)+1)+" is "+str(number))
                print("\nThe final row "+str(i+1) + ":")
                print(sudoku[i,:])
            result = sudoku
    elif mode==1:
        for i in range(0,9):
            # Searching columns for single missing values
            if (np.sum(np.isin(sudoku[:,i],default))) == 8:
                print("The initial column "+str(i+1) + ":")
                print(sudoku[:,i])
                number = 45 - np.sum(sudoku[:,i])
                location = np.argwhere(sudoku[:,i]==0)
                sudoku[:,i] = np.where(sudoku[:,i]==0, number, sudoku[:,i])
                print("\nThe missing value at location "+str(np.asscalar(location)+1)+" is "+str(number))
                print("\nThe final column "+str(i+1)+":")
                print(sudoku[:,i])
            result = sudoku
    elif mode==2:
        for i in range(0,3):
            for j in range(0,3):
            # Searching the 3x3 arrays for single solutions
                if (np.sum(np.isin(sudoku[j*3:(j*3)+3,i*3:(i*3)+3],default))) == 8:
                    print("The initial slice "+str(i+1)+","+str(j+1)+":")
                    print(sudoku[j*3:(j*3)+3,i*3:(i*3)+3])
                    number = 45 - np.sum(sudoku[j*3:(j*3)+3,i*3:(i*3)+3])
                    location = np.argwhere(sudoku[j*3:(j*3)+3,i*3:(i*3)+3]==0)
                    sudoku[j*3:(j*3)+3,i*3:(i*3)+3] = np.where(sudoku[j*3:(j*3)+3,i*3:(i*3)+3]==0, number, sudoku[j*3:(j*3)+3,i*3:(i*3)+3])
                    print("\nThe missing value at location "+str(np.asscalar(location[0,0]))+","+str(np.asscalar(location[0,1]))+" is "+str(number))
                    print("\nThe initial slice "+str(i+1)+","+str(j+1)+":")
                    print(sudoku[j*3:(j*3)+3,i*3:(i*3)+3])
                result = sudoku
    return result'''


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
                    f.write("\nAt location: column-%d and row-%d put the number %d\r\n" % (i+1,k+1,j)) # Writing instructions
                    np.savetxt(f, sudoku-backup, fmt='%1i') # Graphical instruction
                    backup=np.copy(sudoku) # Replacing the backup with the new puzzle
                    # print(sudoku-backup)
                    # print(sudoku)
                else: # If more than one 0 has been replaced with a -1
                    sudoku[k,i] = np.where(sudoku[k,i]==-1, 0, sudoku[k,i]) # Setting the -1 back to 0


# -------------------------------------------MAIN PROGRAM------------------------------------------
if __name__ == '__main__':

    sudoku_in = np.loadtxt("input.txt", dtype="int") # Reading in sudoku puzzle
    sudoku=np.copy(sudoku_in) # Backing up input sudoku to a working array
    f = open("Instructions.txt","w+") # Opening/creating file for outputing instructions
    f.write("The original puzzle:\r\n")
    default = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) # 1D array of sudoku numbers
    np.savetxt(f, sudoku, fmt='%1i') # 

    # Solving the puzzle
    count = 9
    while (np.any(sudoku==0))==True:
        count += 1
        if count > 10:
            exit()
        print(sudoku)
        column_solver(sudoku, default)
        diff = sudoku-sudoku_in
        f.close()
    #column_solver(sudoku, default)