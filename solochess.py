# This program implements the Solo Chess game.

import random

# The chess-board layout at any time, 4x4 (16 elements)
board = []
# Tags assigned to each piece. 1 (K for killer), 2 (F for food), 0 none 
tags = []
# Static list of chess pieces (Bishop, Knight, Pawn, Queen, Rook)
pieces = [1,2,3,4,5]
# List of free cells from where a given piece can check a given cell
# In (row,col) format
checkCells = []
# Moves to win the game!
moves = []

######
# List of all functions in this file
#
# initBoard()
# showBoard()
# pickRandomPiece()
# placePiece(piece, cell)
# movePiece(cell1, cell2)
# placeAnyPiece(cell)
# placeAnyPieceAnyCell()
# checkCell(row, col)
# bishop(p, q)
# knight(p, q)
# pawn(p, q)
# queen(p, q)
# rook(p, q)
# CheckAdjacentCols(row, col)
# CheckAdjacentRows(row, col):
# buildCheckCellsList(target, piece)
# IsCellFree(row, col)
# createRandomLayout()
#
######

def initBoard():
    del board[:]
    del tags[:]
    del moves[:]
    for i in range(16):
        board.append(0)
        tags.append(0)
    #end for
#end def
    
def showBoard():
    p = "U"
    for i in range(4):
        for j in range(4):
            if (board[i*4+j] == 0):
                p = "0 "
            if (board[i*4+j] == 1):
                p = "B"+str(tags[i*4+j])
            if (board[i*4+j] == 2):
                p = "K"+str(tags[i*4+j])
            if (board[i*4+j] == 3):
                p = "P"+str(tags[i*4+j])
            if (board[i*4+j] == 4):
                p = "Q"+str(tags[i*4+j])
            if (board[i*4+j] == 5):
                p = "R"+str(tags[i*4+j])
            if (board[i*4+j] < 0 or board[i*4+j] > 5):
                p = "U"
            print(p, "  ", end="")
        #end for
        print()
    #end for
#end def

#Add this move to the table of moves
def addMove(K, F):
    moves.append(str(K)+","+str(F))
# end addMove

# Out of the currently placed pieces on the board, pick one at random.
def pickRandomPiece():
    L = []
    for i in range(16):
        if (board[i] != 0):
            L.append(i+1)
        #end if
    #end for
    return random.choice(L)
#end pickRandomPiece

    
def removePiece(cell):
    board[cell-1] = 0
    tags[cell-1] = 0
    print("Removed piece at ", cell)
#end placePiece


def placePiece(piece, cell, tag):
    board[cell-1] = piece
    tags[cell-1] = tag
    print("Placed ", piece, " at ", cell)
#end placePiece

# Move along with its tag    
def movePiece(cell1, cell2):
    print("Moving ", board[cell1-1], " from ", cell1, " to ", cell2)
    board[cell2-1] = board[cell1-1]
    board[cell1-1] = 0
    tags[cell2-1] = tags[cell1-1]
    tags[cell1-1] = 0
#end movePiece

# Place any piece at "cell" and assign its tag
def placeAnyPiece(cell, tag):
    board[cell-1] = random.choice(pieces)
    tags[cell-1] = tag
    print("Placed ", board[cell-1], " at ", cell)
#end placeAnyPiece

# Place any piece at any cell and assign 0 as its tag
def placeAnyPieceAnyCell():
    cell = random.choice(range(15))
    board[cell] = random.choice(pieces)
    tags[cell] = 0
    print("Placed ", board[cell], " at ", cell+1)
    return cell+1
#end placeAnyPieceAnyCell

# Convert from [row, col] format to a location number
def getLocation(cell):
    l = cell.split(",")
    location = ((int(l[0])-1)*4)+int(l[1])
    return location
#def getLocation

# Check if the given cell is free (i.e. unoccupied).
def checkCell(row, col):
    if (IsCellFree(row, col) == True):
            checkCells.append(str(row)+","+str(col))
    else:
            return True
    #end if
    return False
#end checkCell


# Build a list of free cells from where a rook can check the given
# target cell.
def rook(p, q):
    # Scan this row
    col = q - 1
    stopscan = False
    while (stopscan != True):
        stopscan = checkCell(p, col)
        col = col - 1
    #end while
    col = q + 1
    stopscan = False
    while (stopscan != True):
        stopscan = checkCell(p, col)
        col = col + 1
    #end while

    # Scan this column
    row = p - 1
    stopscan = False
    while (stopscan != True):
        stopscan = checkCell(row, q)
        row = row - 1
    #end while
    row = p + 1
    stopscan = False
    while (stopscan != True):
        stopscan = checkCell(row, q)
        row = row + 1
    #end while
#end rook

# Build a list of free cells from where a knight can check the given
# target cell.
def knight(p, q):
    Row = p-2
    CheckAdjacentCols(Row, q)
    Row = p+2
    CheckAdjacentCols(Row, q)
    Col = q-2
    CheckAdjacentRows(p, Col)
    Col = q+2
    CheckAdjacentRows(p, Col)
#end knight

def CheckAdjacentCols(row, col):
    if (IsCellFree(row, col-1) == True):
        checkCells.append(str(row)+","+str(col-1))
    if (IsCellFree(row, col+1) == True):
        checkCells.append(str(row)+","+str(col+1))
#end CheckAdjacentCols
                      
def CheckAdjacentRows(row, col):
    if (IsCellFree(row-1, col) == True):
        checkCells.append(str(row-1)+","+str(col))
    if (IsCellFree(row+1, col) == True):
        checkCells.append(str(row+1)+","+str(col))
#end CheckAdjacentRows

# Build a list of free cells from where a queen can check the given
# target cell.
def queen(p, q):
    bishop(p, q)
    rook(p, q)
#end bishop


# Build a list of free cells from where a pawn can check the given
# target cell.
def pawn(p, q):
    if (IsCellFree(p+1, q-1) == True):
        checkCells.append(str(p+1)+","+str(q-1))
    if (IsCellFree(p+1, q+1) == True):
        checkCells.append(str(p+1)+","+str(q+1))
#end def

# Build a list of free cells from where a bishop can check the given
# target cell.
def bishop(p, q):
    # Scan upper rows
    i = 1
    Stopleft = Stopright = False
    while (p-i != 0):
        if ((Stopleft == False) and (IsCellFree(p-i, q-i) == True)):
            checkCells.append(str(p-i)+","+str(q-i))
        else:
            Stopleft = True
        #end if
        if ((Stopright == False) and (IsCellFree(p-i, q+i) == True)):
            checkCells.append(str(p-i)+","+str(q+i))
        else:
            Stopright = True
        #end if
        i = i + 1
    #end while

    # Scan lower rows
    i = 1
    Stopleft = Stopright = False
    while (p+i != 5):
        if ((Stopleft == False) and (IsCellFree(p+i, q-i) == True)):
            checkCells.append(str(p+i)+","+str(q-i))
        else:
            Stopleft = True
        #end if
        if ((Stopright == False) and (IsCellFree(p+i, q+i) == True)):
            checkCells.append(str(p+i)+","+str(q+i))
        else:
            Stopright = True
        #end if
        i = i + 1
    #end while
#end def



# Check the given target cell with any piece.
# This involves:
# 1) Make a temporary list of all pieces
# 2) Try one piece P at a time for steps 3 & 4
# 3) Build a list of check cells for P (using buildCheckCellsList).
# 4) Pick one of these cells and place the given piece there.
def checkCellWithAnyPiece(target, tag):
    retCode = 0
    # Make a copy of the list of pieces
    tempL = pieces[:]
    while (retCode == 0 and len(tempL) > 0):
        piece = random.choice(tempL)
        tempL.remove(piece)
        buildCheckCellsList(target, piece)
        if (len(checkCells) > 0):
            # Place piece at any cell from this list
            newcell = getLocation(random.choice(checkCells))
            placePiece(piece, newcell, tag)
            retCode = newcell
        #endif
    #end while
    return retCode
#end checkCellWithAnyPiece


# Check the given target cell with the given piece.
# This involves building a list of check cells (using buildCheckCellsList).
# And then pick one of these cells and place the given piece there.
# Update global lists appropriately.
def checkCellWithPiece(target, piece, tag):
    buildCheckCellsList(target, piece)
    if (len(checkCells) > 0):
        # Place piece at any cell from this list
        newcell = getLocation(random.choice(checkCells))
        placePiece(piece, newcell, tag)
        return newcell
    else:
        return 0
    #endif
#end checkCellWithPiece

# Build a list of free cells from where the given piece can check the given
# target cell.
def buildCheckCellsList(target, piece):
    # Empty the list
    del checkCells[:]

    p = (int((target - 1) / 4) + 1)
    q = ((target - 1) % 4) + 1

    if (piece == 1):
        # List for bishop
        bishop(p, q)
    #endif
    if (piece == 2):
        # List for knight
        knight(p, q)
    #endif
    if (piece == 3):
        # List for pawn
        pawn(p, q)
    #endif
    if (piece == 4):
        # List for queen
        queen(p, q)
    #endif
    if (piece == 5):
        # List for rook
        rook(p, q)
    #endif
#end def

# Return true if the cell is free, else false.
def IsCellFree(row, col):
    if (row < 1 or row > 4 or col < 1 or col > 4):
        return False
    if (board[((row-1)*4)+col-1] == 0):
        return True
    else:
        return False
#end def

# Get piece
def getPiece(cell):
    return board[cell-1]
#end setTag

# Get tag
def getTag(cell):
    return tags[cell-1]
#end setTag

# Set tag
def setTag(cell, tag):
    tags[cell-1] = tag
#end setTag

# Create the initial layout with N pieces
def createRandomLayout(N):
    # Put a random piece P at a random free cell C.
    cell = placeAnyPieceAnyCell()
    # Assign random tag: 1 (K for killer) or 2 (F for food)
    setTag(cell, random.choice([1,2]))

    # Repeat from here
    for i in range(N):
        showBoard()
        # If tag is "killer" move piece to any cell from where
        # it can check "cell".
        if (getTag(cell) == 1):
            newcell = checkCellWithPiece(cell, getPiece(cell), 1)
            if (newcell > 0):
                # Remove existing piece (since we effectively moved it above)
                removePiece(cell);
                # Put a random piece at "cell"; tag it as "food"
                placeAnyPiece(cell, 2)
                addMove(newcell, cell)
            #endif

        # If tag is "food" put any piece at any free cell from where
        # it can check "cell"; tag it as "killer"
        elif (getTag(cell) == 2):
            newcell = checkCellWithAnyPiece(cell, 1)
            if (newcell > 0):
                addMove(newcell, cell)
        #endif

        # Pick one of the existing pieces on the board.
        cell = pickRandomPiece()
        if (getTag(cell) != 1): 
            # Assign a new random tag
            setTag(cell, random.choice([1,2]))
        #endif
        N = N - 1
    #end for
#end createRandomLayout

def runProgram(N):
    initBoard()
    createRandomLayout(N)
    showBoard()
    print(moves)
    makeMoves()
    showBoard()
#end

def makeMoves():
    for i in range(len(moves)):
        move = moves[-1].split(",")
        del moves[-1]
        movePiece(int(move[0]), int(move[1]))
        del move[:]
    #end for
#end


