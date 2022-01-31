#3d tic tac toe
#
import check_win_3D as tic
"""
example 4 by 4 by 4 grid

          z1  z2  z3  z4
x1        _______________
    y1   |___|___|___|___|
    y2   |___|___|_o_|___|
    y3   |___|_x_|___|___|
    y4   |___|___|___|___|

 _______________
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|

 _______________
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|

 _______________
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|


examplePlane= [['','','',''],['','','',''],['','','',''],['','','','']]
each sublist is a row

exampleGrid = [[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']]]
first sublist is plane, second is row, elements are columns

"""

def printPlane(PlaneList,count):
    print('          z1  z2  z3  z4')
    print('x' + str(count) + str('        _______________')) 
    rowcount=0  
    for row in PlaneList:
        rowcount+=1
        rowstring=('    y' + str(rowcount) + str('   |_'))
        for element in row:
            if element!='':
                rowstring+=str(element) + '_|_'
            else:
                rowstring+='__|_'
        rowstring = rowstring[0:26]
        print(rowstring)

def printGrid(GridList):
    xcount=0
    for plane in GridList:
        xcount+=1
        printPlane(plane,xcount)
        print("")

def mark(grid,symbol,coordinates):
    #grid in example list format
    #symbol as a string, 1 character
    #coordinates in [x,y,z] format
    #where x is plane from top to bottom, y is row from top to bottom and z is column from left to right
    #starting with 1
    try:
        x,y,z = coordinates[0] -1 ,coordinates[1]-1 ,coordinates[2]-1 
        grid[x][y][z] = symbol
    except IndexError: #subtract again
        x,y,z = coordinates[0] -2,coordinates[1]-2 ,coordinates[2]-2 
        grid[x][y][z] = symbol
        
    return grid

def checkinteger(x): #check integer x, if int, return true
    try:
        xint=int(x)
        return True
    except ValueError:
        return False

def checkMoveNotTake(grid,coordinates): #check if move is taken, true if possible to play on
    try:
        x,y,z = coordinates[0] -1 ,coordinates[1]-1 ,coordinates[2]-1 
        if grid[x][y][z]!='':
            return False
        else:
            return True
    except IndexError:
        x,y,z = coordinates[0] -2 ,coordinates[1]-2 ,coordinates[2]-2
        if grid[x][y][z]!='':
            return False
        else:
            return True

def check_move_not_take2(grid,coordinates): #coordinates from 0-3
    try:
        x,y,z = coordinates[0] ,coordinates[1] ,coordinates[2]
        if grid[x][y][z]!='':
            return False
        else:
            return True
    except IndexError:
        x,y,z = coordinates[0] -1 ,coordinates[1]-1 ,coordinates[2]-1
        if grid[x][y][z]!='':
            return False
        else:
            return True

def getCoordinates(grid): #grid data needed to know if move has been taken
    while True:
        coordinateString = input("Enter coordinates in form 'x,y,z': ")
        if len(coordinateString)!=5: #check length for proper format
            print("Invalid format")
        elif coordinateString[1] and coordinateString[3] != ',': #make sure it has commas
            print("Invalid format")

        else:
            coordinateList=[]
            valid = 0 #valid is intially false
            for x in range(len(coordinateString)): #iterate through string
                if coordinateString[x]!=',': #if its not the comma
                    if checkinteger(coordinateString[x]):
                        if (int(coordinateString[x])<5 and int(coordinateString[x])!=0):
                            valid += 1 #count valid integer coordinate
                            coordinateList.append(int(coordinateString[x]))
                    
            if valid==3 and checkMoveNotTake(grid,coordinateList): #must have THREE integer coordinates
                break
            else:
                print('Invalid move')
    return coordinateList

def getSymbol():
    while True:
        symbol = input("Enter symbol to use for the game: ")
        if len(symbol)!=1:
            print("Invalid format")
        else:
            print("Are you sure you want to use '" + symbol + "' as the symbol for the game?")
            if input("(y/n): ") == 'y':
                break

    return symbol

def check_tied_game(grid):
    """
    return true if game is tied"""
    tied = True
    for x in range(4):
        for y in range(4):
            for z in range(4):
                if grid[x][y][z]=='':
                    tied = False
    return tied

def play_multiplayer_game():
    print("""Welcome to 3D Tic Tac Toe!
Player one please enter symbol first""")
    player1symbol = getSymbol()
    print("Player two please enter symbol")
    while True: #loop in case same symbol
        player2symbol = getSymbol()
        if player1symbol==player2symbol:
            print("Symbol cannot be the same as player 1")
        else:
            break

    print("""
Instructions
Moves are determined by coordinates in the form 'x,y,z' 
The first cooridinate is the plane from top to bottom
The second coordinate is the row from top to bottom
The third coordinate is the column from left to right
I.e 1,1,1 would be the left uppermost move""")

    grid  = [[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']]]
    printGrid(grid) #initial board
    allplayer1moves = [] #for memory
    allplayer2moves= [] #for memory 
    while True:

        newgrid=grid.copy()
        j = newgrid.copy()
        
        print("Player 1:")
        player1move=getCoordinates(grid) #get coordinates
        allplayer1moves.append(player1move) #store move in list
        grid = mark(grid,player1symbol,player1move) #implement the move
        printGrid(grid) #show grid 

        if tic.check_all_wins(grid,player1symbol):
            print("Player 1 wins! ")
            #print(grid)
            break

        print("Player 2: ")
        player2move=getCoordinates(grid) #get coordinates
        allplayer2moves.append(player2move) #store move in list
        grid = mark(grid,player2symbol,player2move) #implement the move
        printGrid(grid) #show grid

        if tic.check_all_wins(grid,player2symbol):
            print("Player 2 wins! ")
            break

        #print(allplayer1moves)
        #print(allplayer2moves)

        choice = input("Press 'q' to quit or 'b' to undo ") #choice to end or undo
        if  choice == 'q': #end game
            print("Game ended")
            #print(grid)
            break

        if choice == 'b': #go back
            goBack = int(input("Enter number of times to go back "))
            if goBack>len(allplayer2moves): #cant go back that many moves
                print('Invalid choice, keep playing')
            else: 
                for x in range(goBack): #make the last move empty
                    grid = mark(grid,'',allplayer1moves[-1]) 
                    grid = mark(grid,'',allplayer2moves[-1])
                    allplayer1moves.pop() #then delete the move from the memory 
                    allplayer2moves.pop()
            #print(allplayer1moves)
            #print(allplayer2moves)
                printGrid(grid) #show new grid after going back moves
 
