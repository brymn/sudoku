#sample 'complete' sudoku puzzle. 
#values were replaced with 'None' to assesss the checker function
sudoku = \
           [None,4,5,None,2,7,None,9,8,\
            8,None,9,6,5,4,None,2,7,\
            6,7,2,9,1,8,5,4,3,\
            4,9,6,1,8,5,3,7,None,\
            2,None,8,4,7,3,9,5,6,\
            7,5,3,2,9,6,4,8,1,\
            3,6,7,5,4,2,8,1,9,\
            9,8,4,7,6,1,2,3,5,\
            5,2,1,8,3,9,7,6,4]

#iterates through the sudoku list and creates sub lists
#containing individual rows
masterRows = []
for i in range(0,80,9):
    singleRow = []
    for j in range(0,9):
        singleRow.append(sudoku[i+j])
    masterRows.append(singleRow)

#same as above, but for columns
masterColumns = []
for i in range (0,9):
    singleColumn = []
    for j in range(0,80, 9):
        singleColumn.append(sudoku[i+j])
    masterColumns.append(singleColumn)

#naming could be improved
#marks the index for the upper left (0) digit of each inner grid
firstOfInnerGrids = [0,3,6,27,30,33,54,57,60]

#designates the steps required for obtaining values within each grid
#based on starting from the upper left of each grid
stepsOfInnerGrids = [0,1,2,9,10,11,18,19,20]

#creates an empy list which will be populated with sublists containing distinct grids
#initial loop denotes the 'row' 
#initiates the empty list
#initiates the empty list
#assigns the 'i' value while looping, issues arose when trying to assign in the calculation
#step iterates along the row
#appends to the empty list at the index of the row+column
#appends the newly populated sublist to the master list.
masterGrids = []
for i in range(0,9):
    singleGrid = []
    start = firstOfInnerGrids[i]
    for j in range(0,9):
        step = stepsOfInnerGrids[j]
        singleGrid.append(sudoku[start+step])
    masterGrids.append(singleGrid)

#print(masterGrids)

#designates the values that will be required for each section
possibleValues = [1,2,3,4,5,6,7,8,9]

#validates correct assignments were collected
#for row in masterRows:
#   print(row)

#initiates the three empty lists which will contain the 
#'missing' values indicating that one of the required values
#is not present in the set.
missingRows = []
missingColumns = []
missingGrids = []

#this can definitely be abstracted into a function. It is just repeated
#for simplicity
for row in masterRows:
    missingRow = []
    for i in possibleValues:
        if i not in row:
            missingRow.append(i)
    missingRows.append(missingRow)
    

for column in masterColumns:
    missingColumn = []
    for i in possibleValues:
        if i not in column:
            missingColumn.append(i)
    missingColumns.append(missingColumn)

for grid in masterGrids:
    missingGrid = []
    for i in possibleValues:
        if i not in grid:
            missingGrid.append(i)
    missingGrids.append(missingGrid)

#I know this can be generated, which would be more ideal in that 
#we should be able program this for different size puzzles.
#it dissapoints that this was hard coded but I wasn't able to 
#conceive of the properly nested loops
gridCoordinates ={
    0:{'x': 0, 'y':0, 'grid':0},
    1:{'x': 0, 'y':1, 'grid':0},
    2:{'x': 0, 'y':2, 'grid':0},
    3:{'x': 0, 'y':3, 'grid':1},
    4:{'x': 0, 'y':4, 'grid':1},
    5:{'x': 0, 'y':5, 'grid':1},
    6:{'x': 0, 'y':6, 'grid':2},
    7:{'x': 0, 'y':7, 'grid':2},
    8:{'x': 0, 'y':8, 'grid':2},
    9:{'x': 1, 'y':0, 'grid':0},
    10:{'x': 1, 'y':1, 'grid':0},
    11:{'x': 1, 'y':2, 'grid':0},
    12:{'x': 1, 'y':3, 'grid':1},
    13:{'x': 1, 'y':4, 'grid':1},
    14:{'x': 1, 'y':5, 'grid':1},
    15:{'x': 1, 'y':6, 'grid':2},
    16:{'x': 1, 'y':7, 'grid':2},
    17:{'x': 1, 'y':8, 'grid':2},
    18:{'x': 2, 'y':0, 'grid':0},
    19:{'x': 2, 'y':1, 'grid':0},
    20:{'x': 2, 'y':2, 'grid':0},
    21:{'x': 2, 'y':3, 'grid':1},
    22:{'x': 2, 'y':4, 'grid':1},
    23:{'x': 2, 'y':5, 'grid':1},
    24:{'x': 2, 'y':6, 'grid':2},
    25:{'x': 2, 'y':7, 'grid':2},
    26:{'x': 2, 'y':8, 'grid':2},
    27:{'x': 3, 'y':0, 'grid':3},
    28:{'x': 3, 'y':1, 'grid':3},
    29:{'x': 3, 'y':2, 'grid':3},
    30:{'x': 3, 'y':3, 'grid':4},
    31:{'x': 3, 'y':4, 'grid':4},
    32:{'x': 3, 'y':5, 'grid':4},
    33:{'x': 3, 'y':6, 'grid':5},
    34:{'x': 3, 'y':7, 'grid':5},
    35:{'x': 3, 'y':8, 'grid':5},
    36:{'x': 4, 'y':0, 'grid':3},
    37:{'x': 4, 'y':1, 'grid':3},
    38:{'x': 4, 'y':2, 'grid':3},
    39:{'x': 4, 'y':3, 'grid':4},
    40:{'x': 4, 'y':4, 'grid':4},
    41:{'x': 4, 'y':5, 'grid':4},
    42:{'x': 4, 'y':6, 'grid':5},
    43:{'x': 4, 'y':7, 'grid':5},
    44:{'x': 4, 'y':8, 'grid':5},
    45:{'x': 5, 'y':0, 'grid':3},
    46:{'x': 5, 'y':1, 'grid':3},
    47:{'x': 5, 'y':2, 'grid':3},
    48:{'x': 5, 'y':3, 'grid':4},
    49:{'x': 5, 'y':4, 'grid':4},
    50:{'x': 5, 'y':5, 'grid':4},
    51:{'x': 5, 'y':6, 'grid':5},
    52:{'x': 5, 'y':7, 'grid':5},
    53:{'x': 5, 'y':8, 'grid':5},
    54:{'x': 6, 'y':0, 'grid':6},
    55:{'x': 6, 'y':1, 'grid':6},
    56:{'x': 6, 'y':2, 'grid':6},
    57:{'x': 6, 'y':3, 'grid':7},
    58:{'x': 6, 'y':4, 'grid':7},
    59:{'x': 6, 'y':5, 'grid':7},
    60:{'x': 6, 'y':6, 'grid':8},
    61:{'x': 6, 'y':7, 'grid':8},
    62:{'x': 6, 'y':8, 'grid':8},
    63:{'x': 7, 'y':0, 'grid':6},
    64:{'x': 7, 'y':1, 'grid':6},
    65:{'x': 7, 'y':2, 'grid':6},
    66:{'x': 7, 'y':3, 'grid':7},
    67:{'x': 7, 'y':4, 'grid':7},
    68:{'x': 7, 'y':5, 'grid':7},
    69:{'x': 7, 'y':6, 'grid':8},
    70:{'x': 7, 'y':7, 'grid':8},
    71:{'x': 7, 'y':8, 'grid':8},
    72:{'x': 8, 'y':0, 'grid':6},
    73:{'x': 8, 'y':1, 'grid':6},
    74:{'x': 8, 'y':2, 'grid':6},
    75:{'x': 8, 'y':3, 'grid':7},
    76:{'x': 8, 'y':4, 'grid':7},
    77:{'x': 8, 'y':5, 'grid':7},
    78:{'x': 8, 'y':6, 'grid':8},
    79:{'x': 8, 'y':7, 'grid':8},
    80:{'x': 8, 'y':8, 'grid':8},
} 

#identifies where a value is missing, identifies which values could possibly be in that row, 
#then checks against the associated column and identifies which values could be in that row.
#if a value could be in the row but not the column, it is identified.
#Future variations of this will also check against the inner grid and remove values
#insert known values into the puzzle and remove incorrect values from 'possible' lists.  
for index in gridCoordinates:
    xValue = gridCoordinates[index]['x']
    yValue = gridCoordinates[index]['y']
    if sudoku[index] == None:
        for possible in possibleValues:
            if possible in missingRows[xValue]:
                if possible not in missingColumns[yValue]:
                    print(missingRows)
                    print("absolute index " + str(index) + " can not be " + str(possible))