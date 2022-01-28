#check win 3d ttt
#import tictactoe as toe


"""
There are a few ways to win

4 by 4 grid shown
Plane row *4 
Plane column *4
Plane diagonal *4

4 by 4 grid orthongonal to screen, up and down
Column Plane column *4 
Column Plane row == plane column *considered
Column Plane diagonal *4

4 by 4 grid orthogonal to screen, left to right
Row Plane column == column plane column *considered
Row Plane row === plane row *considered
Row Plane diagonal *4

Cube diagonal *4

"""


emptyGrid = [[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']]]
example1  = [[['x', 'o', '', ''], ['x', 'o', '', ''], ['x', 'o', '', ''], ['x', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', 'o']]]
example2  = [[['x', 'x', 'x', 'x'], ['', '', 'o', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', 'o', 'o'], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', 'o']]]
example3  = [[['', '', '', ''], ['x', 'x', 'x', 'x'], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', 'o', 'o', 'o'], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', 'o']]]
example4  = [[['x', '', '', ''], ['', 'x', 'o', ''], ['', '', 'x', ''], ['', '', '', 'x']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', 'o', 'o', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', 'o']]]
example5  = [[['o', '', '', 'x'], ['', '', 'x', ''], ['', 'x', '', ''], ['x', '', '', '']], [['', '', '', ''], ['', 'o', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['o', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', 'o']]]
example6  = [[['', 'o', '', ''], ['', 'x', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', 'x', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', 'x', '', ''], ['', '', 'o', ''], ['o', '', '', '']], [['', '', '', ''], ['', 'x', '', ''], ['', '', '', ''], ['', '', '', 'o']]]
example7  = [[['o', 'o', 'x', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', 'x', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', 'x', ''], ['', '', '', '']], [['o', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', 'x', 'o']]]
example8  = [[['o', 'o', 'o', 'o'], ['', '', '', ''], ['', '', '', ''], ['', '', '', 'x']], [['', '', '', ''], ['', '', '', ''], ['', '', '', 'x'], ['', '', '', '']], [['', '', '', ''], ['', '', '', 'x'], ['', '', '', ''], ['', '', '', '']], [['', '', '', 'x'], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]]
example9  = [[['o', 'o', '', ''], ['x', '', '', ''], ['', 'o', '', ''], ['', '', '', '']], [['', '', '', ''], ['', 'x', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', 'x', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', 'x'], ['', '', '', ''], ['', '', '', 'o']]]
example10 = [[['o', '', '', 'x'], ['o', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', 'x', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', 'x', '', ''], ['o', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['x', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', 'o']]]
example11 = [[['x', 'o', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', 'x', 'o', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', 'x', 'o'], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', 'o', '', 'x']]]
example12 = [[['', '', 'o', 'x'], ['', '', 'o', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', 'x', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['o', '', '', ''], ['', 'x', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['x', '', '', 'o']]]
example13 = [[['x', 'o', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['x', 'o', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['x', 'o', '', ''], ['', '', '', ''], ['', '', '', '']], [['x', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]]
example14 = [[['x', '', '', 'o'], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['x', '', '', 'o'], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['x', '', 'o', ''], ['x', '', '', 'o'], ['', '', '', '']], [['x', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', 'o']]]
example15 = [[['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['x', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['x', '', '', ''], ['', '', '', '']], [['x', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['x', 'o', 'o', 'o']]]
example16 = [[['x', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['x', '', '', '']], [['', '', '', ''], ['x', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', 'o', ''], ['x', '', '', 'o'], ['', '', '', '']], [['x', '', '', ''], ['', '', '', ''], ['', 'o', '', ''], ['x', 'o', 'o', 'o']]]
example17 = [[['', 'o', '', ''], ['', '', '', ''], ['', '', '', ''], ['x', '', '', '']], [['', '', '', ''], ['', 'o', '', ''], ['x', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['x', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['x', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', 'o', 'o']]]
example18 = [[['x', '', '', 'o'], ['x', 'x', '', ''], ['', '', 'x', ''], ['x', '', '', 'x']], [['', '', '', ''], ['', 'o', 'o', ''], ['', 'o', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', 'o', ''], ['', '', '', ''], ['', '', '', 'o']]]

def sum_list(list):
    sum=0
    for element in list:
        sum+=element
    #print(sum)
    list_copy  = list[:]
    list_copy2 = list[:]
    list_copy.sort() #elements are ascending 
    list_copy2.sort( reverse = True) #elements are descending 
    if (list_copy == list or list_copy2 ==list) and sum==6: #must be one or the other and sum to 6
        return sum
    else:
        return 0

def check_plane_row(grid,symbol):
    win =False
    for x in range(4): #iterate through planes
        for y in range(4): #iterate through rows
            rowcount=0
            for z in range(4): #iterate through columns
                if grid[x][y][z] == symbol:
                    rowcount+=1
                    #print("counted " + str(grid[x][y][z]))
                    if rowcount==4:
                        win = True
                        print("way 1")
    return win

def check_plane_column(grid,symbol):
    win = False
    for x in range(4): #iterate through grids
        for z in range(4): #iterate through columns
            columncount=0
            for y in range(4): #iterate through rows
                if grid[x][y][z] == symbol:
                    columncount+=1
                    if columncount==4:
                        win = True
                        print("way 2")
    return win

def check_plane_diag(grid,symbol):
    win = False
    #true diagonal
    for x in range(4): #iterate through grids
        diagcount=0
        for y in range(4): #iterate through rows
            for z in range(4): #iterate through columns:
                if grid[x][y][z]== symbol and (y==z): # or y+z==3): #if index is same 
                    diagcount+=1
                    #print("here")
                    #print(diagcount)
                    if diagcount==4:
                        win = True
                        print("way 3.1")

    #inverse diagonal
    for x in range(4): #iterate through grids
        diagcount2=0
        for y in range(4): #iterate through rows
            for z in range(4): #iterate through columns:
                if grid[x][y][z]== symbol and y+z==3: 
                    #print("BROOOO")
                    #   sum is 3 because inverse 
                    #   consider 1,1,4 -> last two indices add to 5
                    #   subtract 2 because real indcies start at 0, not 1
                    #   therefore sum or inverse diagonal indices should be 3
                    #print('counted ' + str(x) + str(y) + str(z))
                    diagcount2+=1
                    if diagcount2==4:
                        win = True
                        print("way 3.2")
    #print(diagcount)
    return win

def check_column_plane_column(grid,symbol):
    win =False
    for z in range(4): #iterate through columns
        for y in range(4): #iterate through rows
            columncount=0
            for x in range(4): #iterate up grids
                if grid[x][y][z]==symbol:
                    columncount+=1
                    if columncount==4:
                        win = True
                        print("way 4")
    return win

def check_column_plane_diag(grid,symbol):
    win =False
    rowcount =[] #ensure rows are ascending order
    rowcount2 = [] #for inverse diagonal where x+y ==3

    #first is to check 'true' diagonal
    for z in range(4): #iterate through columns
        diagcount=0
        for x in range(4): #iterate through grids
            for y in range(4): #iterate through rows
                if grid[x][y][z]==symbol and (x==y ):# or x+y==3):
                   diagcount+=1
                   rowcount.append(y)
                   #print("diag count: " + str(diagcount))
                   #print(sum_list(rowcount))
                   if diagcount==4 and sum_list(rowcount)==6: #ensure diagonal is one way
                       #indices must be in ascending order for rows
                       #thus sum = 0 + 1 + 2 + 3 =6
                        win = True
                        #print("row count: " + str(rowcount))
                        print("way 5.1")

    #now check inverse diagonal
    for z in range(4): #iterate through columns
        diagcount=0
        for x in range(4): #iterate through grids
            for y in range(4): #iterate through rows
                if grid[x][y][z]==symbol and (x+y==3):
                   diagcount+=1
                   rowcount2.append(y)
                   #print("diag count2: " + str(diagcount))
                   #print("row count2 " + str(rowcount2))
                   if diagcount==4 and sum_list(rowcount2)==6: #ensure diagonal is one way
                       #indices must be in ascending order for rows
                       #thus sum = 0 + 1 + 2 + 3 =6
                        win = True
                        #print("row count2: " + str(rowcount2))
                        print("way 5.2")
    
    #print("row count: " + str(rowcount))
    #print("diag count: " + str(diagcount))
    return win

def check_row_plane_diag(grid,symbol):
    win = False
    columncount=[]
    columncount2 = []

    #true diagonal
    for y in range(4): #iterate through rows
        diagcount=0
        for x in range(4): #iterate through grids
            for z in range(4): #iterate through columns
                if grid[x][y][z]==symbol and (x==z): # or x+z==3):
                    diagcount+=1
                    columncount.append(z)
                    if diagcount==4 and sum_list(columncount)==6:
                        win = True
                        #print("column count1 " + str(columncount))
                        print("way 6.1")

    #inverse diagonal
    for y in range(4): #iterate through rows
        diagcount=0
        for x in range(4): #iterate through grids
            for z in range(4): #iterate through columns
                if grid[x][y][z]==symbol and x+z==3:
                    diagcount+=1
                    columncount2.append(z)
                    if diagcount==4 and sum_list(columncount2)==6:
                        win = True
                        print("column count2 " + str(columncount2))
                        print("way 6.1")
        
    return win 

def check_true_diag(grid,symbol):
    win = False
    diagcount=0
    for x in range(4): #iterate through grids
        for y in range(4): #iterate through rows
            for z in range(4): #iterate through columns
                if grid[x][y][z]==symbol and (x==y and y==z):
                    diagcount+=1
                    if diagcount==4:
                        win = True
                        print("way 7")
    return win 

def check_cube_diag(grid,symbol):
    win = False
    if   grid[0][0][3]==symbol and grid[1][1][2]==symbol and grid[2][2][1]==symbol and grid[3][3][0]==symbol:
        win = True
        print("way 8")

    elif grid[0][3][0]==symbol and grid[1][2][1]==symbol and grid[2][1][2]==symbol and grid[3][0][3]==symbol:
        win = True
        print("way 9")

    elif grid[0][3][3]==symbol and grid[1][2][2]==symbol and grid[2][1][1]==symbol and grid[3][0][0]==symbol:
        win = True
        print("way 10")
    return win

def check_all_wins(grid,symbol):
    if check_plane_row(grid,symbol):
        return True
    if check_plane_column(grid,symbol):
        return True
    if check_plane_diag(grid,symbol):
        return True
    if check_column_plane_column(grid,symbol):
        return True
    if check_column_plane_diag(grid,symbol):
        return True
    if check_row_plane_diag(grid,symbol):
        return True
    if check_true_diag(grid,symbol):
        return True
    if check_cube_diag(grid,symbol):
        return True
    else:
        return False

