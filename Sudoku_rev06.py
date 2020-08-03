# Sudoku_rev06.py - Sudoku Problem solver
#
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
            return missing'=

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
    box_3x3 > 0
    line_3x3 = np.reshape(box_3x3,(1,9))
    sort_line = np.sort(line_3x3)
#    print(sort_line)
    zeros_removed = sort_line[sort_line > 0]
#    print("3x3 Check - zeros removed = ",zeros_removed)
    #row_list = zeros_removed
    #print("Row list in function: ",row_list)
    return zeros_removed





#-------------------------------------------------------------------------------
#  Read input file and store in a 9x9 numpy array
sudoku_9x9_in=np.genfromtxt("9x9_in.csv", delimiter=',')
sudoku_9x9_in=sudoku_9x9_in.astype('int32')
#print(sudoku_9x9_in)

point_x = 0
point_y = 0
solved_count = 0
not_solved_count = 0
solved_hold = 0

while True:
    point = sudoku_9x9_in[point_y,point_x]
    print("Y=",point_y," X",point_x," value = ",point)
    if point == 0:
        print("Zero Found")
    else:
        print("Not a zero")


    point_x += 1
    if point_x == 9:
        point_x = 0
        point_y += 1
#        print("Y=",point_y," X",point_x," this should end")
        if point_y == 9:
            print("Loop end break hit. Solved = ",solved_count)
            if solved_hold == solved_count:
                break
            if not_solved_count > 0:
                point_y = 0
                solved_hold = solved_count
                not_solved = 0
                continue
            else:
                break
        continue








"""
    if  point == 0:
#        print("zero Found - Location:  Y=",point_y," X=",point_x)
        zeros_removed = check_row(point_y)
#        print(zeros_removed)
        if len(zeros_removed) == 8:
            insert_answer(point_y,point_x)
            solved_count += 1
            point_y += 1
            point_x = 0
            if point_y == 9:
                point_y = 0
                not_solved = 0
#                print("Y=",point_y," X",point_x," Reset the loop")
            continue   #forces restart of loop
        else:
            row_values = zeros_removed
#        print("Multiple zeros in row check column")
        zeros_removed = check_column(point_x)
#        print("Column check = ",zeros_removed)
        if len(zeros_removed) == 8:
            insert_answer(point_y,point_x)
            solved_count += 1
            #point_y += 1
            point_x += 1
            if point_x == 9:
                point_x = 0
                point_y += 1
#                print("Y=",point_y," X",point_x," this should end")
                if point_y == 9:
                    print("Column break hit")
                    break
            continue   #forces restart of loop
        else:
            column_values = zeros_removed
            existing_values = np.concatenate((column_values,row_values))
            existing_dups_removed = np.unique(existing_values)
    #        print("Column and Row : ",existing_dups_removed)
            if len(existing_dups_removed) == 8:
                insert_answer(point_y,point_x)
                solved_count += 1
                point_y += 1
                point_x = 0
                if point_y == 9:
                    point_y = 0
                    not_solved = 0
    #                print("Y=",point_y," X",point_x," Reset the loop")
                continue   #forces restart of loop
            else:
                row_values = zeros_removed

#        print("Multiple zeros in row and column check 3x3")
        zeros_removed = check_3x3(point_y,point_x)
#        print("Successfully returned from 3x3 check")
        if len(zeros_removed) == 8:
            insert_answer(point_y,point_x)
            solved_count += 1
            #point_y += 1
            point_x += 1
            if point_x == 9:
                point_x = 0
                point_y += 1
#                print("Y=",point_y," X",point_x," this should end")
                if point_y == 9:
                    print("3x3 break hit")
                    break
            continue   #forces restart of loop
        else:
            values_3x3 = zeros_removed
            all_existing = np.concatenate((values_3x3,existing_dups_removed))
            all_uniques = np.unique(all_existing)
            print("Y=",point_y," X=",point_x,"  All existing = ",all_uniques)

            if len(all_uniques) == 8:
                zeros_removed = all_uniques
                insert_answer(point_y,point_x)
                solved_count += 1
            #    point_y += 1
                point_x += 1
                if point_x == 9:
                    point_y += 1
                    point_x = 0
                    not_solved = 0
                    if point_y == 9:
                        print("3x3 break hit")
                        break
            #                print("Y=",point_y," X",point_x," Reset the loop")
                continue   #forces restart of loop





            not_solved += 1









#            point_y += 1
#            point_x = 0
#            continue

    point_x += 1
    if point_x == 9:
        point_x = 0
        point_y += 1
#        print("Y=",point_y," X",point_x," this should end")
        if point_y == 9:
            print("Loop end break hit. Solved = ",solved_count)
            if solved_hold == solved_count:
                break
            if not_solved > 0:
                point_y = 0
                solved_hold = solved_count
                not_solved = 0
                continue
            else:
                break
        continue
#    print("Y=",point_y," X=",point_x," at While end")
"""

print("The Final Answer:")
print("Solved for : ",solved_count)
print("Still not solved : ",not_solved_count)
print(sudoku_9x9_in)
