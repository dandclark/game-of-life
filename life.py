import sys
import os.path
import time

DEAD_CELL_CHAR = '.'
LIVE_CELL_CHAR = 'X'
LINES_TO_CLEAR = 40
LINES_TO_CENTER = 20

def readGrid(filename):
    '''
    Reads a grid from a text file
    '''
    if not os.path.isfile(filename):
        exit('Could not find ' + filename)
    file = open(filename)
    grid = [[]]
    currentRow = 0
    nextChar = file.read(1)
    while nextChar != "":
        if nextChar == '\n':
            currentRow += 1
            grid.append([])
        else:
            grid[currentRow].append(nextChar)
        nextChar = file.read(1)
    file.close()
    if not grid[-1]:
        grid.pop()
    print grid
    return grid


def displayGrid(grid):
    ''''
    Given a two-dimensional array, prints it as
    a grid.  Assumes grid is square.
    '''
    for i in range(len(grid)):
        for j in range(len(grid)):
            print grid[i][j],
        print

def adjacentCount(grid, x, y, char):
    '''
    Returns the number of instances of char
    lie adjacent to the square x, y in the grid.
    '''
    result = 0
    
    if y > 0:
        if grid[x][y-1] == char:
            result += 1
    if y < len(grid) - 1:
        if grid[x][y+1] == char:
            result += 1

    if x > 0:
        if grid[x-1][y] == char:
            result += 1
        if y > 0:
            if grid[x-1][y-1] == char:
                result += 1
        if y < len(grid) - 1:
            if grid[x-1][y+1] == char:
                result += 1
    if x < len(grid) - 1:
        if grid[x+1][y] == char:
            result += 1
        if y > 0:
            if grid[x+1][y-1] == char:
                result += 1
        if y < len(grid) - 1:
            if grid[x+1][y+1] == char:
                result += 1
    return result

def doTurn(grid):
    newGrid = [ [] for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            newCell = grid[i][j]
            liveNeighbors = adjacentCount(grid, i, j, LIVE_CELL_CHAR)
            if grid[i][j] == LIVE_CELL_CHAR:
                if liveNeighbors < 2:
                    newCell = DEAD_CELL_CHAR # Cell dies from underpopulation
                elif liveNeighbors < 4:
                    newCell = LIVE_CELL_CHAR # Cell lives on
                else:
                    newCell = DEAD_CELL_CHAR # Cell dies from overpopulation
            elif grid[i][j] == DEAD_CELL_CHAR:
                if liveNeighbors == 3:
                    newCell = LIVE_CELL_CHAR # New cell is spawned
            newGrid[i].append(newCell)
    return newGrid

if len(sys.argv) < 2:
    exit('Usage: python ' + sys.argv[0] + ' <seed file name>')

theGrid = readGrid(sys.argv[1])

displayGrid(theGrid)

while True:
    theGrid = doTurn(theGrid)
    print
    for i in range(LINES_TO_CLEAR):
        print
    displayGrid(theGrid)
    for i in range(LINES_TO_CENTER):
        print
    #raw_input()
    time.sleep(0.2)
