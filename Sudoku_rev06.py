# Sudoku_rev06.py - Sudoku Problem solver
#
#  20200805 - Working on the new idea of solving based on the highist existing
#               number on the board.
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
#  Used to process the input file
import pandas
#  To work with arrays
import numpy as np

import collections, numpy
#-------------------------------------------------------------------------------
def check_row(row_y):
    get_row = sudoku_9x9_in[row_y]
#    print("Row Y=",row_y," = ",get_row)
    sort_row = np.sort(get_row)
#    print(sort_row)
    zeros_removed = sort_row[sort_row > 0]
#    print("In the loop")
    return zeros_removed

def check_column(column_x):
    get_column = sudoku_9x9_in[:,column_x]
#    print("Column X=",column_x," = ",get_column)
    sort_column = np.sort(get_column)
#    print(sort_column)
    zeros_removed = sort_column[sort_column > 0]
#    print("In the loop")
    return zeros_removed

def missing_number(zeros_removed):
    for missing in range(1, 10):
        if missing in zeros_removed:
#            print(missing," is on the list")
#   I need to fix this function so I don't need the if else
            z = 0

        else:
#            print(missing, "is the missing number")
#            x = missing
            return missing

def insert_answer(point_y,point_x):
#    print("Single Zero Found:  Y=",point_y," X=",point_x)
    x = missing_number(zeros_removed)
#            print("Returned missing number is ",x)
    sudoku_9x9_in[point_y,point_x] = x
#            print(sudoku_9x9_in[point_y,point_x])
#        break
    print("End of solve:",x,"at Y=",point_y," X=",point_x)
#    print("The answer:")
#    print(sudoku_9x9_in)

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
#    print("The box is = ",box_y_start," ",box_y_end," ",box_x_start," ",box_x_end)
    box_3x3 = sudoku_9x9_in[box_y_start:box_y_end,box_x_start:box_x_end]
#    print(box_3x3)
#    box_3x3 > 0
#    line_3x3 = np.reshape(box_3x3,(1,9))
#    sort_line = np.sort(line_3x3)
#    print(sort_line)
#    zeros_removed = sort_line[sort_line > 0]
#    print("3x3 Check - zeros removed = ",zeros_removed)
    #row_list = zeros_removed
    #print("Row list in function: ",row_list)
    return box_3x3

def number_count():
    number_hold = 0
    for i in range (1, 10):
        number_check = np.count_nonzero(sudoku_9x9_in == i)
#        print("count ",i," = ",np.count_nonzero(sudoku_9x9_in == i))
#        print("Count ",i," = ",number_check)
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
#print(sudoku_9x9_in)

point_x = 0
point_y = 0
#solved_count = 0
#not_solved_count = 0
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
            print("End Right Here")
            break
        continue
    else:
        print("Row Y = ",point_y," possible solve")
        print("Y=",point_y," X",point_x," value = ",solve_number)
        #----------temp patch
        if point_x == 9:
            break
        #------------------


        # --- This is the column loop looking for a possible solve column
        point_x = 0    #this resets the columns when swithing from row checks
        while True:
            get_column = sudoku_9x9_in[:,point_x]
            #print("Column X = ",point_x," - ",get_column)
            if solve_number in get_column:
                point_x += 1
                if point_x == 9:
                    break
                continue
            else:
                print("Column X = ",point_x," possible solve")

                # --- Row and Column found --- check the 3x3 loop
                get_box = check_3x3(point_y,point_x)
                print(get_box)
                if solve_number in get_box:
                    print("Solve Number is in the box")
                    point_x += 1
                    if point_x == 9:
                        break
                    continue
                else:
                    # --- Double check the row
                    get_row = sudoku_9x9_in[point_y]
                    print("Double Check Row Y = ",point_y," - ",get_row)
                    if solve_number in get_row:
                        point_x += 1
                        if point_x == 9:
                            break
                        continue
                    else:
                        print("Y=",point_y," X",point_x," value = ",solve_number)
                        sudoku_9x9_in[point_y,point_x] = solve_number

                        break


        #  this next line will need to move
        #point_y += 1


    if point_y == 9:
        break

    continue








print("The Final Answer:")
print(sudoku_9x9_in)


"""
    point_x += 1
    if point_x == 9:
        point_x = 0
        point_y += 1
#        print("Y=",point_y," X",point_x," this should end")
        if point_y == 9:
            zeros_remaining = np.count_nonzero(sudoku_9x9_in == 0)
            print("Loop End Zeros Remaining = ",zeros_remaining)
            if zero_hold == zeros_remaining:
                break
            else:
                zero_hold = zeros_remaining
                point_y = 0
                continue
        continue
"""
