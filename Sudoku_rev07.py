# Sudoku_rev07.py - Sudoku Problem solver
#
#  20200810 - Starting Rev08 - This logic is working but limited it is not
#               forward thinking enough to select the proper solution if
#               more than one exists.
#  20200808 - Cleaning up code.... I am getting close i hope
#  20200805 - Working on the new idea of solving based on the highist existing
#               number on the board.
#               Started rev07.  Rev06 is working for a single number
#  20200803 - Dug into numpy to count numbers in array - still working on code
#  20200802 - Rev6 - total rebuild.  There is a logic error in finding the
#               number to solve for.  The code is getting messy so taking
#               what I know and cleaning up and stream lining.
#  20200801 - Rev04 is working but can't solve the entire problem.
#               moving to Rev05
#  20200731 - Checking for the last 0 (missing number) in a 3x3 grid.  More
#               testing is needed but that can wait for tomorrow.
#  20200730 - Successfully check and solving if a row has a single zero in rev02
#               rev03 will expand to colmn check logic - working for columns
#               rev04 will includ 3x3 check for a single missing zero
#  20200729 - New revisoin because the code was working and I don't want
#             to mess that up when I introduce a do while true loop
#  20200726 - Renamed this because I messed this up beyond recovery.
#  20200725 - started converting to functions - code not working with pushed
#  20200720 - I moved the code out of the 100DaysOfCode.  It will be easier to
#             track it this way.  Converted input to numpy
##
#
################################################################################
#
#  Needed to open the input file
import os
# Used to process the input file
import pandas
#  To work with arrays
import numpy as np

import collections, numpy
#-------------------------------------------------------------------------------
#convert a 3x3 box to a list
def check_3x3(point_y,point_x):
    if point_y < 3:
        box_y_start = 0
        box_y_end = 3
    elif point_y < 6:
        box_y_start = 3
        box_y_end = 6
    else:
        box_y_start = 6
        box_y_end = 9
    if point_x < 3:
        box_x_start = 0
        box_x_end = 3
    elif point_x < 6:
        box_x_start = 3
        box_x_end = 6
    else:
        box_x_start = 6
        box_x_end = 9
    box_3x3 = sudoku_9x9_in[box_y_start:box_y_end,box_x_start:box_x_end]
    return box_3x3

def number_count():
    number_hold = 0
    for i in range (1, 10):
        number_check = np.count_nonzero(sudoku_9x9_in == i)
#        print("count ",i," = ",np.count_nonzero(sudoku_9x9_in == i))
        print("Count ",i," = ",number_check)
#        print("Number Hold = ",number_hold)
        if number_check > number_hold and number_check < 9:
            george = i
            number_hold = number_check
#            print("Solve for = ",george)
    return george

#-------------------------------------------------------------------------------
#  Read input file and store in a 9x9 numpy array
sudoku_9x9_in=np.genfromtxt("9x9_in.csv", delimiter=',')
sudoku_9x9_in=sudoku_9x9_in.astype('int32')

point_x = 0
point_y = 0
zero_hold = 0

solve_number = number_count()
print("Solve for = ",solve_number)

while True:
    #  ---- this is the row loop looking for the solve row
    get_row = sudoku_9x9_in[point_y]
    #print("Row Y=",point_y," = ",get_row)
    #print(solve_number in get_row)
    if solve_number in get_row:
        point_y += 1
        if point_y == 9:
            #print("End Right Here")
            #break

            point_y = 0


            zeros_remaining = np.count_nonzero(sudoku_9x9_in == 0)
            print("Loop End Zeros Remaining = ",zeros_remaining)
            if zero_hold == zeros_remaining:
                solve_number = number_count()
                print("The Next Solve Number is = ",solve_number)
                continue
            else:
                zero_hold = zeros_remaining
                point_y = 0
                continue

        continue
    else:
        print("Row Y = ",point_y," possible solve")
        #print("Y=",point_y," X",point_x," value = ",solve_number)
        point_x = 0    #this resets the columns
        #----------temp patch
        if point_x == 9:
            print("unexpected end stop with X=9")
            break

        #--------------------------------------------------------------------
        # --- This is the column loop looking for a possible solve column
        #--------------------------------------------------------------------
        while True:
            get_column = sudoku_9x9_in[:,point_x]
            #print("Column X = ",point_x," - ",get_column)
            if solve_number in get_column:
                point_x += 1
                if point_x == 9:
                    print("Row nine hit end row check")
                    row_y = 9 #  this will kill the loop  delete late
                    break
                continue
            else:
                print("Column X = ",point_x," possible solve")
                # --- check the value of the position
                if sudoku_9x9_in[point_y,point_x] > 0:
                    print("Y=",point_y," X",point_x," ----Value Exists")
                    point_x += 1
                    if point_x == 9:
                        break
                    continue
                # --- Row and Column found --- check the 3x3 loop
                get_box = check_3x3(point_y,point_x)
                print(get_box)
                if solve_number in get_box:
                    print("Solve Number ",solve_number," is in the box")
                    point_x += 1
                    if point_x == 9:
                        break
                    continue
                else:
                    # --- Double check the row
                #    get_row = sudoku_9x9_in[point_y]
                #    print("Double Check Row Y = ",point_y," - ",get_row)
                #    if solve_number in get_row:
                #        point_x += 1
                #        if point_x == 9:
                #            break
                #        continue
                #   else:
                    if sudoku_9x9_in[point_y,point_x] > 0:
                        print("Y=",point_y," X",point_x," ----Solve Error")
                        continue
                    else:
                        print("Y=",point_y," X",point_x," value = ",solve_number)
                        sudoku_9x9_in[point_y,point_x] = solve_number
                        break
                    break

        #-------------------------------------------------
        # End of the Column while Loop
        #-------------------------------------------------
        #  this next line will need to move
        #point_y += 1


    if point_y == 9:
        break

    continue








print("The Final Answer:")
print(sudoku_9x9_in)
