#Computer ttt
import tictactoe as ttt
import CheckWinTTT as win
import random as ran
import itertools

"""
computer needs to play 
be able to read 'lines'
see lines of intersection POI

recall (x,y,z) where x is plane or elevation, y is row, and z is column 
+- 5 represents line direction, variables represent coordinates

plane column: [x,5,z] DONE
plane row: [x,y,5] DONE
column plane column: [5,y,z] DONE

plane true diagonal: [x,5,5] DONE
plane inverse diagonal: [x,5,-5] DONE

column plane true diagonal: [5,5,z] DONE
column plane inv diag: [5,-5,z] DONE

row plane true diagonal: [5,y,5] DONE
row plane inv diag: [5,y,-5] DONE

cube true diagonal: [5,5,5] 
cube diag2: [5,5,-5] start 1 grid top right
cube diag3: [5,-5,5] start 1 grid bottom left
cube diag4: [5,-5,-5] start 1 grid bottom right
"""

#    ***coordinates are minus 1 since indices start at 0

"""

all functions all return a list in the form
[
    [[a, b, c], [n, [x, y, z]], [n, [x, y, z]], [n, [x, y, z]], [n, [x, y, z]]]
    
    where 
    a,b,c element of {0,1,2,3,5,-5} where 0-3 rep coordinate and +-5 represents direction
    n element of {-1,0,1} where 1 rep player move, 0 rep empty move, -1 rep opponent move
    x,y,z, element of {0,1,2,3} where x,y,z rep coordinate on grid

    i.e 
    [[5, 3, 0], [0, [0, 3, 0]], [0, [1, 3, 0]], [0, [2, 3, 0]], [0, [3, 3, 0]]]

    a=5, thus column plane column
    b=3, c=0, thus at [x,3,0]  
    the following elements all have first sub-element 0, thus move not taken
    the second sub-element is the coordiante in the line
    all points in the line are accounted for
]

"""
def check_plane_row(grid,symbol):
    plane_row_data=[]
    for x in range(4): #iterate through planes
        for y in range(4): #iterate through rows
            line_data=[[x,y,5]]  #line identity and direction
            for z in range(4): #iterate through columns
                if grid[x][y][z] == symbol:
                    line_data.append([1,[x,y,z]])
                elif grid[x][y][z]=='':
                    line_data.append([0,[x,y,z]])
                else:
                    line_data.append([-1,[x,y,z]])
            plane_row_data.append(line_data) #accumulate every lines data
    return plane_row_data

def check_plane_column(grid,symbol):
    plane_column_data=[]
    for x in range(4): #iterate through grids
        for z in range(4): #iterate through columns
            line_data=[[x,5,z]]
            for y in range(4): #iterate through rows
                if grid[x][y][z] == symbol:
                    line_data.append([1,[x,y,z]])
                elif grid[x][y][z]=='':
                    line_data.append([0,[x,y,z]])
                else:
                    line_data.append([-1,[x,y,z]])
            plane_column_data.append(line_data)
    return plane_column_data

def check_column_plane_column(grid,symbol):
    column_plane_column_data=[]
    for z in range(4): #iterate through columns
        for y in range(4): #iterate through rows
            line_data=[[5,y,z]]
            for x in range(4): #iterate up grids
                if grid[x][y][z] == symbol:
                    line_data.append([1,[x,y,z]])
                elif grid[x][y][z]=='':
                    line_data.append([0,[x,y,z]])
                else:
                    line_data.append([-1,[x,y,z]])
            column_plane_column_data.append(line_data)

    return column_plane_column_data


def check_plane_diag(grid,symbol):
    plane_diag_data=[]
    #true diagonal
    for x in range(4): #iterate through grids
        line_data1=[[x,5,5]]
        for y in range(4): #iterate through rows
            for z in range(4): #iterate through columns:
                if y==z:
                    if grid[x][y][z] == symbol:
                        line_data1.append([1,[x,y,z]])
                    elif grid[x][y][z]=='':
                        line_data1.append([0,[x,y,z]])
                    else:
                        line_data1.append([-1,[x,y,z]])
        plane_diag_data.append(line_data1)

    #inverse diagonal
    for x in range(4): #iterate through grids
        line_data2=[[x,5,-5]]
        for y in range(4): #iterate through rows
            for z in range(4): #iterate through columns:
                if y+z==3: 
                    if grid[x][y][z] == symbol:
                        line_data2.append([1,[x,y,z]])
                    elif grid[x][y][z]=='':
                        line_data2.append([0,[x,y,z]])
                    else:
                        line_data2.append([-1,[x,y,z]])
        plane_diag_data.append(line_data2)
    return plane_diag_data

def check_column_plane_diag(grid,symbol):
    column_plane_diag_data=[]
    #first is to check 'true' diagonal
    for z in range(4): #iterate through columns
        line_data1=[[5,5,z]]
        for x in range(4): #iterate through grids
            for y in range(4): #iterate through rows
                if x==y:#true diag
                    if grid[x][y][z] == symbol:
                        line_data1.append([1,[x,y,z]])
                    elif grid[x][y][z]=='':
                        line_data1.append([0,[x,y,z]])
                    else:
                        line_data1.append([-1,[x,y,z]])
        column_plane_diag_data.append(line_data1)

    #now check inverse diagonal
    for z in range(4): #iterate through columns
        line_data2=[[5,-5,z]]
        for x in range(4): #iterate through grids
            for y in range(4): #iterate through rows
                if (x+y==3):
                    if grid[x][y][z] == symbol:
                        line_data2.append([1,[x,y,z]])
                    elif grid[x][y][z]=='':
                        line_data2.append([0,[x,y,z]])
                    else:
                        line_data2.append([-1,[x,y,z]])
        column_plane_diag_data.append(line_data2)
    return column_plane_diag_data

def check_row_plane_diag(grid,symbol):
    row_plane_diag_data=[]
    for y in range(4): #iterate through rows
        line_data1=[[5,y,5]]
        for x in range(4): #iterate through grids
            for z in range(4): #iterate through columns
                if x==z: #true diag
                    if grid[x][y][z] == symbol:
                        line_data1.append([1,[x,y,z]])
                    elif grid[x][y][z]=='':
                        line_data1.append([0,[x,y,z]])
                    else:
                        line_data1.append([-1,[x,y,z]])
        row_plane_diag_data.append(line_data1)

    #inverse diagonal
    for y in range(4): #iterate through rows
        line_data2=[[5,y,-5]]
        for x in range(4): #iterate through grids
            for z in range(4): #iterate through columns
                if x+z==3:
                    if grid[x][y][z] == symbol:
                        line_data2.append([1,[x,y,z]])
                    elif grid[x][y][z]=='':
                        line_data2.append([0,[x,y,z]])
                    else:
                        line_data2.append([-1,[x,y,z]])
        row_plane_diag_data.append(line_data2)
    return row_plane_diag_data 


def check_cube_diag(grid,symbol):
    cube_diag_data=[]
    line_data1=[[5,5,5]]
    line_data2=[[5,5,-5]]
    line_data3=[[5,-5,5]]
    line_data4=[[5,-5,-5]]
    for x in range(4):
        for y in range(4):
            for z in range(4):
                if x==y and y==z: #true diag
                    if grid[x][y][z] == symbol:
                        line_data1.append([1,[x,y,z]])
                    elif grid[x][y][z]=='':
                        line_data1.append([0,[x,y,z]])
                    else:
                        line_data1.append([-1,[x,y,z]])

                if y+z==3 and x+z==3: #line 2
                    #grid[0][0][3]==symbol and grid[1][1][2]==symbol and grid[2][2][1]==symbol and grid[3][3][0]==symbol
                    if grid[x][y][z] == symbol:
                        line_data2.append([1,[x,y,z]])
                    elif grid[x][y][z]=='':
                        line_data2.append([0,[x,y,z]])
                    else:
                        line_data2.append([-1,[x,y,z]])
                elif x+y==3 and z+y==3: #line 3
                #grid[0][3][0]==symbol and grid[1][2][1]==symbol and grid[2][1][2]==symbol and grid[3][0][3]==symbol:
                    if grid[x][y][z] == symbol:
                        line_data3.append([1,[x,y,z]])
                    elif grid[x][y][z]=='':
                        line_data3.append([0,[x,y,z]])
                    else:
                        line_data3.append([-1,[x,y,z]])

                elif y+x==3 and z+x==3: #line 4
                #grid[0][3][3]==symbol and grid[1][2][2]==symbol and grid[2][1][1]==symbol and grid[3][0][0]==symbol
                    if grid[x][y][z] == symbol:
                        line_data4.append([1,[x,y,z]])
                    elif grid[x][y][z]=='':
                        line_data4.append([0,[x,y,z]])
                    else:
                        line_data4.append([-1,[x,y,z]])
    cube_diag_data.append(line_data1)
    cube_diag_data.append(line_data2)
    cube_diag_data.append(line_data3)
    cube_diag_data.append(line_data4)
    return cube_diag_data




    for line in type_line_data:
        print(line)
#end of group of line functions

def get_cube_data(grid,symbol): #returns list that has ALL group of lines data
    #symbol is bot symbol
    cube_data=[]

    plane_rows_data = check_plane_row(grid,symbol)
    plane_column_data= check_plane_column(grid,symbol)
    column_plane_column_data=check_column_plane_column(grid,symbol)

    plane_diag_data= check_plane_diag(grid,symbol)
    column_plane_diag_data = check_column_plane_diag(grid,symbol)
    row_plane_diag_data = check_row_plane_diag(grid,symbol)

    cube_diag_data = check_cube_diag(grid,symbol)

    cube_data.append(plane_rows_data)
    cube_data.append(plane_column_data)
    cube_data.append(column_plane_column_data)
    cube_data.append(plane_diag_data)
    cube_data.append(column_plane_diag_data)
    cube_data.append(row_plane_diag_data)
    cube_data.append(cube_diag_data)
    return cube_data


def read_accumulated_data(type_line_data): #reads group and prints each line
    for line in type_line_data:
        print(line)

def read_cube_data(cube_data): #reads all groups and prints each group with empty line inbetween
    for type_of_win in cube_data:
        read_accumulated_data(type_of_win)
        print("")



def check_poi(line1_,line2_): #checks if lines intersect, if they do, returns true and POI in list [boo,coordinate]
    """
    example line data:
    [[0, 0, 5], [0, [0, 0, 0]], [-1, [0, 0, 1]], [0, [0, 0, 2]], [0, [0, 0, 3]]]
    [[0, 5, 0], [0, [0, 0, 0]], [0, [0, 1, 0]], [0, [0, 2, 0]], [1, [0, 3, 0]]]

    """
    POI_boo = False #assume lines dont intersect
    POI=''
    line1=line1_[:]
    line2=line2_[:]
    del line1[0]
    del line2[0]
    for coordinate in line1:
        for coordinate2 in line2:
            if coordinate[1] == coordinate2[1]:
                POI_boo = True
                POI = coordinate[1]
    return [POI_boo,POI]

def count_moves_on_line(line_): #count's player and opponents move on a line
    #returns player and opponent count in list [play,op]
    bot_count=0
    opponent_count=0
    line=line_[:]
    del line[0]
    for coordinate in line:
        if coordinate[0] ==1:
            bot_count+=1
        elif coordinate[0]==-1:
            opponent_count+=1
    return [bot_count,opponent_count]

def possible_win_line(line_): #check if it is possible to win on this line, returns boo
    line=line_[:]
    win=True #initially probably can win
    player=False #initially probably no moves on it yet
    opponent=False # ditto
    del line[0]

    for coordinate in line:
        #print(coordinate[1])
        if coordinate[0]==1:
            player=True
            #print("player move ")
        elif coordinate[0]== -1:
            #print("opponent move")
            opponent=True
    if player and opponent: #if both players on it, impossible to win
        win=False
    return win

def block_move(line_): #opponent has three in a row 
    """
    return block move coordinate
    """
    line=line_[:]
    del line[0]
    for coordinate in line:
        if coordinate[0] != -1:
            return coordinate[1]

def check_threat(cube_data): #check if opponent is about to win
    """
    return true if 3 in row, and block coordinate
    else, return false and ''
    [boo,coordinate]
    """
    threat = False
    coordinate= ''
    for group in cube_data:
        for line in group:
            count = count_moves_on_line(line)
            if count[1]==3 and count[0]==0:
                threat = True
                coordinate = block_move(line)
    return [threat,coordinate]


def empty_move(line_):
    """
    return block move coordinate
    """
    line=line_[:]
    del line[0]
    for coordinate in line:
        if coordinate[0] != 1: #not already the bot's move
            return coordinate[1]

def check_easy_win_cube(cube_data):
    """
    return true if 3 in row, and easy win
    else, return false and ''
    [boo,coordinate]
    """
    easy_win = False
    coordinate= ''
    for group in cube_data:
        for line in group:
            count = count_moves_on_line(line)
            if count[0]==3 and count[1]==0: #bot has 3, opponent/player has none therefore one empty
                easy_win = True
                coordinate = empty_move(line)
    return [easy_win,coordinate]

def check_bot_2_in_row(cube_data):
    """
    return true if 3 in row, and easy win
    else, return false and ''
    [boo,coordinate]
    """
    two_in_line = False
    coordinate= ''
    for group in cube_data:
        for line in group:
            count = count_moves_on_line(line)
            if count[0]==2 and count[1]==0: #bot has 2, opponent/player has none therefore two empty
                two_in_line = True
                coordinate = empty_move(line)
    return [two_in_line,coordinate]

def compare_list_of_lines(grid,set_of_lines): #check poi for a list of lines
    """
    grid needed to know if poi is taken
    return [boo,coordinate]
    true if intersect, false if not
    """
    threat_poi=[False,''] 

    mylist = range(len(set_of_lines))
    for x,y in itertools.combinations(mylist, 2):
        test_POI = check_poi(set_of_lines[x],set_of_lines[y]) #check if they intersect and at what coordinate

        if test_POI[0] and ttt.check_move_not_take2(grid,test_POI[1]): #lines intersect and poi is availible
            threat_poi[0] = test_POI[0]
            threat_poi[1] = test_POI[1]

    return threat_poi         

def check_2_in_line_poi_threat(grid,cube_data): #check if opponent might win using 2 lines that intersect 
    """
    return true if opponent has 2 lines have 2 moves and intersect and poi is not taken
    else, return false and ''
    [boo,coordinate]
    """
    threat = False
    coordinate = ''

    potential_opponent_lines = []
    for group in cube_data:
        for line in group:
            count = count_moves_on_line(line)
            if count[1]==2 and count[0]==0: #opponent has 2 on this line and bot has none
                potential_opponent_lines.append(line)

    poi_boo_coordinate = compare_list_of_lines(grid,potential_opponent_lines) 
    if poi_boo_coordinate[0]:
        threat = True
        coordinate = poi_boo_coordinate[1]
    return [threat,coordinate]


"""Method to block planes
Next order of business is blocking the "plane strategy"

 _______________
|___|___|___|___|
|___|_x_|_x_|___|
|___|_x_|_x_|___|
|___|___|___|___|

Once opponent has this on any plane, it is game over
Unless bot has two blocks on each side like
 _______________
|___|___|___|___|
|___|_x_|_x_|___|
|_o_|_x_|_x_|___|
|___|___|_o_|___|

Therefore we want to block when it gets to:
 _______________
|___|___|___|___|
|___|_x_|_x_|___|
|___|_x_|___|___|
|___|___|___|___|

To do this we need to collect data, again
Not data on every line, but every plane...

[x,y,z] where p represents dimension plane is in and variable represents location

4 normal planes [0,p,p]

4 column planes [p,p,0] 

4 row planes [p,0,p]
"""

#functions shall immediatly check if there is a threat -> 3 
#first, corresponding helper functions
def check_normal_plane_blocked_outside(grid,opponent_symbol,x): #return True if blocked
    """return true if blocked"""
    row_block_count=0 #outside rows, y
    column_block_count=0 #outside columns, z
    blocked=False
    for y in range(4): #iterate through rows
        for z in range(4): #iterate through columns
            if (y==0 or y==3) and 0<z<3:
                if grid[x][y][z]!=opponent_symbol and grid[x][y][z]!='':
                    row_block_count+=1
            if (z==0 or z==3) and 0<y<3:
                if grid[x][y][z]!=opponent_symbol and grid[x][y][z]!='':
                    column_block_count+=1
    if (row_block_count >=1 )and column_block_count >=1:
        blocked = True
    return blocked

def check_column_plane_blocked_outside(grid,opponent_symbol,z):
    """return true if blocked"""
    blocked=False
    outside_column=0 #y
    outside_grid=0 #x
    for y in range(4): #iterate through rows
        for x in range(4): #iterate through grids
            if (y==0 or y==3) and 0<x<3: #outside grids
                if grid[x][y][z]!=opponent_symbol and grid[x][y][z]!='':
                    outside_grid+=1
            if (x==0 or x==3) and 0<y<3: #outside columns
                if grid[x][y][z]!=opponent_symbol and grid[x][y][z]!='':
                    outside_column+=1
    if outside_column>=1 and outside_grid>=1:
        blocked = True
    return blocked

def check_row_plane_blocked_outside(grid,opponent_symbol,y):
    """return true if blocked"""
    blocked=False
    outside_row=0 #z
    outside_grid=0 #x
    for x in range(4): #iterate through grids
        for z in range(4): #iterate through columns
            if (x==0 or x==3) and 0<z<3: #outside rows
                if grid[x][y][z]!=opponent_symbol and grid[x][y][z]!='':
                    outside_row+=1
            if (z==0 or z==3) and 0<x<3: #outside grids
                if grid[x][y][z]!=opponent_symbol and grid[x][y][z]!='':
                    outside_grid+=1
    if outside_row>=1 and outside_grid>=1:
        blocked = True
    return blocked


def check_normal_plane_threat(grid,opponent_symbol): 
    """
    return [boo,cordinate]
    true if threat, coordinate block move
    """
    threat= False
    move_to_block = ''
    for x in range(4): #iterate through grids
        center_count=0 #count the opponent moves in the critical centre moves
        bot_count=0
        for y in range(4):
            for z in range(4):
                if y==z and (0<y<3 and 0<z<3): #true diag
                    if grid[x][y][z]==opponent_symbol: #opponents move
                        center_count+=1 
                    elif grid[x][y][z]!='': #not opponent move nor empty, bot move
                        bot_count+=1

                elif y+z==3 and (0<y<3 and 0<z<3): #inverse
                    if grid[x][y][z]==opponent_symbol: #opponent
                        center_count+=1
                    elif grid[x][y][z]!='': #not opponent move nor empty, bot move
                        bot_count+=1
        
        if center_count==3: #there are three in critical position
            for i in range(2): #quickly iterate to find the empty 
                for j in range(2): #just itereate through the 4
                    if grid[x][i+1][j+1]=='':
                        move_to_block=[x,i+1,j+1]

        blocked_outside = check_normal_plane_blocked_outside(grid,opponent_symbol,x)
        if not blocked_outside: #not blocked on outside
            if bot_count==0: #not already blocked on inside
                if center_count==3: #already has three in position
                    threat = True #there is a threat

    return [threat,move_to_block]

def check_column_plane_threat(grid,opponent_symbol):
    """
    return [boo,cordinate]
    true if threat, coordinate block move
    """
    threat= False
    move_to_block = ''
    for z in range(4): #iterate through different columns
        opponent_count=0
        bot_count=0
        for x in range(4):
            for y in range(4):
                if x==y and (0<y<3 and 0<x<3): #true diag
                    if grid[x][y][z]==opponent_symbol: #opponents move
                        opponent_count+=1 
                    elif grid[x][y][z]!='': #not opponent move nor empty, bot move
                        bot_count+=1

                elif x+y==3 and (0<y<3 and 0<x<3): #inverse
                    if grid[x][y][z]==opponent_symbol: #opponent
                        opponent_count+=1
                    elif grid[x][y][z]!='': #not opponent move nor empty, bot move
                        bot_count+=1

        if opponent_count==3: #there are three in critical position
            for i in range(2): #quickly iterate to find the empty 
                for j in range(2): #just itereate through the 4
                    if grid[i+1][j+1][z]=='':
                        move_to_block=[i+1,j+1,z]
        
        blocked_outside = check_column_plane_blocked_outside(grid,opponent_symbol,z)
        if not blocked_outside: #not blocked on outside
            if bot_count==0: #not already blocked on inside
                if opponent_count==3: #already has three in position
                    threat = True #there is a threat
    
    return [threat,move_to_block]

def check_row_plane_threat(grid,opponent_symbol):
    """
    return [boo,cordinate]
    true if threat, coordinate block move
    """
    threat= False
    move_to_block = ''
    for y in range(4): #iterate through different rows
        opponent_count=0
        bot_count=0
        for z in range(4):
            for x in range(4):
                if z==x and (0<x<3 and 0<z<3): #true diag
                    if grid[x][y][z]==opponent_symbol: #opponents move
                        opponent_count+=1 
                    elif grid[x][y][z]!='': #not opponent move nor empty, bot move
                        bot_count+=1

                elif x+z==3 and (0<x<3 and 0<z<3): #inverse
                    if grid[x][y][z]==opponent_symbol: #opponent
                        opponent_count+=1
                    elif grid[x][y][z]!='': #not opponent move nor empty, bot move
                        bot_count+=1
            
        if opponent_count==3: #there are three in critical position
            for i in range(2): #quickly iterate to find the empty 
                for j in range(2): #just itereate through the 4
                    if grid[i+1][y][j+1]=='':
                        move_to_block=[i+1,y,j+1]
        
        blocked_outside = check_row_plane_blocked_outside(grid,opponent_symbol,y)
        if not blocked_outside: #not blocked on outside
            if bot_count==0: #not already blocked on inside
                if opponent_count==3: #already has three in position
                    threat = True #there is a threat
    return [threat,move_to_block]


"""6 diagonal planes
Due to the complexity, I have no idea how to express these planes
I shall refer to them using the following examples:
"""
"""diag plane example 1,2
 _______________
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|

 _______________
|___|___|___|___|
|___|_x_|___|___|   #1,1,1
|___|_x_|___|___|   #1,2,1
|___|___|___|___|

 _______________
|___|___|___|___|
|___|___|_x_|___|   #2,1,2
|___|___|_x_|___|   #2,2,2
|___|___|___|___|

 _______________
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|

outside_diag1 =  [[[0,1,0],[0,2,0],[3,1,3],[3,2,3]],[[1,0,1],[1,3,1],[2,1,2],[2,2,2]]]
center_diag1  =  [[1,1,1],[1,2,1],[2,1,2],[2,2,2]]
_______________________________________

 _______________
|___|___|___|___|
|___|___|___|_o_|   #0,1,3
|___|___|___|_o_|   #0,2,3
|___|___|___|___|

 _______________
|___|___|_o_|___|   #1,0,2
|___|___|_x_|___|   #1,1,2
|___|___|_x_|___|   #1,2,2
|___|___|___|___|   #1,3,2

 _______________
|___|___|___|___|
|___|_x_|___|___|   #2,1,1
|___|_x_|___|___|   #2,2,1
|___|___|___|___|

 _______________
|___|___|___|___|
|_o_|___|___|___|   #3,1,0
|___|___|___|___|
|___|___|___|___|

outside_diag2 = [[[3,1,0],[3,2,0],[0,1,3],[0,2,3]],[[1,0,2],[1,3,2],[2,0,1],[2,3,1]]]
center_diag2  = [[1,1,2],[1,2,2],[2,1,1],[2,2,1]]
"""
"""diag plane example 3,4
 _______________
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|

 _______________
|___|___|___|___|
|___|_x_|_x_|___|   #1,1,1
|___|___|___|___|   #1,1,2
|___|___|___|___|

 _______________
|___|___|___|___|
|___|___|___|___|   #2,2,1
|___|_x_|_x_|___|   #2,2,2
|___|___|___|___|

 _______________
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|

outside_diag3 = [[[0,0,1],[0,0,2],[3,3,1],[3,3,2]],[[1,1,0],[1,1,3],[2,2,0],[2,2,3]]]
center_diag3  = [[2,2,2],[2,2,1],[1,1,1],[1,1,2]]
______________________________________________

 _______________
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|

 _______________
|___|___|___|___|
|___|___|___|___|   #1,2,1
|___|_x_|_x_|___|   #1,2,2
|___|___|___|___|

 _______________
|___|___|___|___|
|___|_x_|_x_|___|   #2,1,1
|___|___|___|___|   #2,1,2
|___|___|___|___|

 _______________
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|

outside_diag4 = [[[3,0,1],[3,0,2],[0,3,1],[0,3,2]],[[2,1,0],[2,1,3],[1,2,0],[1,2,3]]]
center_diag4  = [[1,2,1],[1,2,2],[2,1,1],[2,1,2]]
"""
"""diag plane example 5,6
_______________
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|

 _______________
|___|___|___|___|
|___|_x_|___|___|   #1,1,1
|___|___|_x_|___|   #1,2,2
|___|___|___|___|

 _______________
|___|___|___|___|
|___|_x_|___|___|   #2,1,1
|___|___|_x_|___|   #2,2,2
|___|___|___|___|

 _______________
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|

outside_diag5 = [[[0,1,1],[0,2,2],[3,1,1,],[3,2,2]],[[1,0,0],[1,3,3],[2,0,0],[2,3,3]]]
center_diag5  = [[2,1,1,],[2,2,2],[1,1,1],[1,2,2]]
______________________________________________

 _______________
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|

 _______________
|___|___|___|___|
|___|___|_x_|___|   #1,1,2
|___|_x_|___|___|   #1,2,1
|___|___|___|___|

 _______________
|___|___|___|___|
|___|___|_x_|___|   #2,1,2
|___|_x_|___|___|   #2,2,1
|___|___|___|___|

 _______________
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|
|___|___|___|___|

outside_diag6 = [[[0,1,2],[0,2,1],[3,1,2],[3,2,1]],[[1,0,3],[1,3,0],[2,0,3],[2,3,0]]]
center_diag6  = [[2,1,2],[2,2,1],[1,1,2],[1,2,1]]
"""


def check_diag_plane_threat(grid,opponent_symbol,center_diag_plane,outside_diag_plane):
    """
    input grid data, opponent symbol and diagonal plane to check
    return [boo,cordinate]
    true if threat, coordinate block move
    """
    opponent_count=0
    bot_count= 0 

    block_outside1=0
    block_outside2=0
    blocked_outside = False

    threat= False
    move_to_block = ''
    for x in range(4):
        for y in range(4):
            for z in range(4):
                if [x,y,z] in center_diag_plane:
                    if grid[x][y][z] == opponent_symbol:
                        opponent_count+=1
                    elif grid[x][y][z]!='':
                        bot_count+=1
                if [x,y,z] in outside_diag_plane[0]:#on outside 
                    if grid[x][y][z] != '' and grid[x][y][z]!= opponent_symbol:
                        block_outside1+=1
                if [x,y,z] in outside_diag_plane[1]:#on other outside 
                    if grid[x][y][z] != '' and grid[x][y][z]!= opponent_symbol: #neither empty nor opponent
                        block_outside2+=1
    if block_outside1>=1 and block_outside2>=1:
        blocked_outside = True
    
    if opponent_count==3 and bot_count!=1 and not blocked_outside:
        threat = True
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    if [x,y,z] in center_diag_plane:
                        if grid[x][y][z] == '':
                            move_to_block = [x,y,z]
    
    return [threat,move_to_block]
    
def check_all_plane_threats(grid,opponent_symbol):
    """
    input grid data, opponent symbol
    return [boo,cordinate]
    true if threat, coordinate block move
    """
    outside_diag1 = [[[0,1,0],[0,2,0],[3,1,3],[3,2,3]],[[1,0,1],[1,3,1],[2,1,2],[2,2,2]]]
    center_diag1  = [[1,1,1],[1,2,1],[2,1,2],[2,2,2]]
    outside_diag2 = [[[3,1,0],[3,2,0],[0,1,3],[0,2,3]],[[1,0,2],[1,3,2],[2,0,1],[2,3,1]]]
    center_diag2  = [[1,1,2],[1,2,2],[2,1,1],[2,2,1]]
    outside_diag3 = [[[0,0,1],[0,0,2],[3,3,1],[3,3,2]],[[1,1,0],[1,1,3],[2,2,0],[2,2,3]]]
    center_diag3  = [[2,2,2],[2,2,1],[1,1,1],[1,1,2]]
    outside_diag4 = [[[3,0,1],[3,0,2],[0,3,1],[0,3,2]],[[2,1,0],[2,1,3],[1,2,0],[1,2,3]]]
    center_diag4  = [[1,2,1],[1,2,2],[2,1,1],[2,1,2]]
    outside_diag5 = [[[0,1,1],[0,2,2],[3,1,1],[3,2,2]],[[1,0,0],[1,3,3],[2,0,0],[2,3,3]]]
    center_diag5  = [[2,1,1,],[2,2,2],[1,1,1],[1,2,2]]
    outside_diag6 = [[[0,1,2],[0,2,1],[3,1,2],[3,2,1]],[[1,0,3],[1,3,0],[2,0,3],[2,3,0]]]
    center_diag6  = [[2,1,2],[2,2,1],[1,1,2],[1,2,1]]
    p1 = check_normal_plane_threat(grid,opponent_symbol)
    p2 = check_column_plane_threat(grid,opponent_symbol)
    p3 = check_row_plane_threat(grid,opponent_symbol)
    d1 = check_diag_plane_threat(grid,opponent_symbol,center_diag1,outside_diag1)
    d2 = check_diag_plane_threat(grid,opponent_symbol,center_diag2,outside_diag2)
    d3 = check_diag_plane_threat(grid,opponent_symbol,center_diag3,outside_diag3)
    d4 = check_diag_plane_threat(grid,opponent_symbol,center_diag4,outside_diag4)
    d5 = check_diag_plane_threat(grid,opponent_symbol,center_diag5,outside_diag5)
    d6 = check_diag_plane_threat(grid,opponent_symbol,center_diag6,outside_diag6)
    if p1[0]:
        return p1
    if p2[0]:
        return p2
    if p3[0]:
        return p3
    elif d1[0]:
        return d1
    elif d2[0]:
        return d2
    elif d3[0]:
        return d3
    elif d4[0]:
        return d4
    elif d5[0]:
        return d5
    elif d6[0]:
        return d6
    else:
        return [False,'']

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

def change_coordinates(coordinates): #change coordinates from real indices to coordinates
    #print("coordinates " , coordinates)
    for x in range(3):
        coordinates[x]+=1
    return coordinates

def bot_decide_move(grid,bot_symbol,opponent_symbol):
    """
    return best bot_move"""
    cube_data = get_cube_data(grid,bot_symbol)
        #read_cube_data(cube_data)

    threat2 = check_2_in_line_poi_threat(grid,cube_data) #poi 2 lines
    if threat2[0]: #there is a threat
        bot_move = change_coordinates(threat2[1])
    
    threat3 = check_all_plane_threats(grid,opponent_symbol) #center of plane 
    if threat3[0]:
        bot_move = change_coordinates(threat3[1])

    threat1 = check_threat(cube_data)           #3 in a row
    if threat1[0]: #there is a threat to block
            #print("THREAT THREAT")
        bot_move = threat1[1] #this is the coordinate
                #element+=1#now coordinates should be 1-4
        bot_move = change_coordinates(bot_move)
            #print(bot_move)

    if not threat1[0] and not threat2[0] and not threat3[0]: #just play random
        bot_2_in_line = check_bot_2_in_row(cube_data)
        if bot_2_in_line[0]:
            print(bot_symbol , " moved to threat")
            bot_move = change_coordinates(bot_2_in_line[1])

        else:
            while True:
                bot_move = [ran.randint(1,4),ran.randint(1,4),ran.randint(1,4)]
                if ttt.checkMoveNotTake(grid,bot_move):
                    print(bot_symbol , " moved random ")
                    break
        
    easy_3_in_row = check_easy_win_cube(cube_data)
    if easy_3_in_row[0]:
        bot_move = change_coordinates(easy_3_in_row[1])
        print(bot_symbol , " moved to win")
    return bot_move
    

def play_game():
    grid  = [[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']]]
    print("Welcome to single player 3D tic tac toe against bot")
    print("Please chose symbol first")
    player_symbol = ttt.getSymbol()
    print("Chose symbol for bot ")
    while True: #loop in case same symbol
        bot_symbol = ttt.getSymbol()
        if player_symbol==bot_symbol:
            print("Bot symbol cannot be the same as yours")
        else:
            break
    print("")
    print("""Instructions
Moves are determined by coordinates in the form 'x,y,z' 
The first cooridinate is the plane from top to bottom
The second coordinate is the row from top to bottom
The third coordinate is the column from left to right
I.e 1,1,1 would be the left uppermost move""")


    ttt.printGrid(grid) #initial board
    allplayer1moves = [] #for memory
    allplayer2moves= [] #for memory 
    while True:

        print("Player:")
        player1move=ttt.getCoordinates(grid) #get coordinates
        allplayer1moves.append(player1move) #store move in list
        grid = ttt.mark(grid,player_symbol,player1move) #implement the move
        #ttt.printGrid(grid) #show grid 

        if win.check_all_wins(grid,player_symbol):
            ttt.printGrid(grid)
            print("Player wins! ")
            #print(grid)
            break
        
        bot_move = bot_decide_move(grid,bot_symbol,player_symbol)
    
        allplayer2moves.append(bot_move)
        grid =ttt.mark(grid,bot_symbol,bot_move)
        ttt.printGrid(grid) #show grid
        print("Bot moved: " + str(bot_move))

        if win.check_all_wins(grid,bot_symbol): #bot win?
            #ttt.printGrid(grid)
            print("Bot wins! ")
            break

        if check_tied_game(grid):
            print("Game tied! ")
            break

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
                    grid = ttt.mark(grid,'',allplayer1moves[-1]) 
                    grid = ttt.mark(grid,'',allplayer2moves[-1])
                    allplayer1moves.pop() #then delete the move from the memory 
                    allplayer2moves.pop()
            #print(allplayer1moves)
            #print(allplayer2moves)
                ttt.printGrid(grid) #show new grid after going back moves

def play_game2():
    grid  = [[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']]]
    print("Welcome to single player 3D tic tac toe against bot")
    print("Please chose symbol first")
    player_symbol = ttt.getSymbol()
    print("Chose symbol for bot ")
    while True: #loop in case same symbol
        bot_symbol = ttt.getSymbol()
        if player_symbol==bot_symbol:
            print("Bot symbol cannot be the same as yours")
        else:
            break
    print("")
    print("""Instructions
Moves are determined by coordinates in the form 'x,y,z' 
The first cooridinate is the plane from top to bottom
The second coordinate is the row from top to bottom
The third coordinate is the column from left to right
I.e 1,1,1 would be the left uppermost move""")


    #ttt.printGrid(grid) #initial board
    allplayer1moves = [] #for memory
    allplayer2moves= [] #for memory 
    while True:
        bot_move = bot_decide_move(grid,bot_symbol)
          
        allplayer2moves.append(bot_move)
        grid =ttt.mark(grid,bot_symbol,bot_move)
        ttt.printGrid(grid) #show grid
        print("Bot moved: " + str(bot_move))

        if win.check_all_wins(grid,bot_symbol): #bot win?
            #ttt.printGrid(grid)
            print("Bot wins! ")
            break

        print("Player:")
        player1move=ttt.getCoordinates(grid) #get coordinates
        allplayer1moves.append(player1move) #store move in list
        grid = ttt.mark(grid,player_symbol,player1move) #implement the move
        #ttt.printGrid(grid) #show grid 

        if win.check_all_wins(grid,player_symbol):
            ttt.printGrid(grid)
            print("Player wins! ")
            #print(grid)
            break

        if check_tied_game(grid):
            print("Game tied! ")
            break

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
                    grid = ttt.mark(grid,'',allplayer1moves[-1]) 
                    grid = ttt.mark(grid,'',allplayer2moves[-1])
                    allplayer1moves.pop() #then delete the move from the memory 
                    allplayer2moves.pop()
            #print(allplayer1moves)
            #print(allplayer2moves)
                ttt.printGrid(grid) #show new grid after going back moves

def spectate_bots():
    grid  = [[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']]]
    ttt.printGrid(grid) #initial board
    all_bot_1_moves = [] #for memory
    all_bot_2_moves= [] #for memory


    print("Welcome to 3D tic tac toe: Spectating bots")
    print("Please chose symbol for bot 1")
    bot_1_symbol = ttt.getSymbol()
    print("Chose symbol for bot 2")
    while True: #loop in case same symbol
        bot_2_symbol = ttt.getSymbol()
        if bot_1_symbol==bot_2_symbol:
            print("Bot symbol cannot be the same as yours")
        else:
            break
    
    while True: #game
        
        bot_move = bot_decide_move(grid,bot_1_symbol,bot_2_symbol)

        all_bot_1_moves.append(bot_move)
        grid =ttt.mark(grid,bot_1_symbol,bot_move)
        #ttt.printGrid(grid) #show grid

        if win.check_all_wins(grid,bot_1_symbol): #bot 1 win?
            ttt.printGrid(grid)
            print("Bot 1 moved: " + str(bot_move))
            print("Bot 1 wins! ")
            break

#REPEAT BUT FOR BOT 2 _______________________________________________________________
        
        bot_2_move = bot_decide_move(grid,bot_2_symbol,bot_1_symbol)

        all_bot_2_moves.append(bot_2_move)
        grid =ttt.mark(grid,bot_2_symbol,bot_2_move)
        ttt.printGrid(grid) #show grid
        print("Bot 1 moved: " + str(bot_move))
        print("Bot 2 moved: " + str(bot_2_move))

        if win.check_all_wins(grid,bot_2_symbol): #bot 2 win?
            #ttt.printGrid(grid)
            print("Bot 2 wins! ")
            break
#___________________________________________________________________________________

        if check_tied_game(grid):
            print("Game tied! ")
            break

        choice = input("Press 'q' to quit or 'b' to undo ") #choice to end or undo
        if  choice == 'q': #end game
            print("Game ended")
            #print(grid)
            break

        if choice == 'b': #go back
            goBack = int(input("Enter number of times to go back "))
            if goBack>len(all_bot_2_moves): #cant go back that many moves
                print('Invalid choice, keep playing')
            else: 
                for x in range(goBack): #make the last move empty
                    grid = ttt.mark(grid,'',all_bot_1_moves[-1]) 
                    grid = ttt.mark(grid,'',all_bot_2_moves[-1])
                    all_bot_1_moves.pop() #then delete the move from the memory 
                    all_bot_2_moves.pop()
            #print(allplayer1moves)
            #print(allplayer2moves)
                ttt.printGrid(grid) #show new grid after going back moves

def play_again():
    while True:
        skip = False
        choice= input("Press 'a' for multiplayer player, 'b' for single player, and 'c' for spectating bots: ")
        if choice == 'a':
            ttt.playGame()
        elif choice == 'b':
            play_game()
        elif choice=='bb':
            play_game2()
        elif choice == 'c':
            spectate_bots()
        else:
            print("Please enter a choice")
            skip = True
        if not skip and input("Would you like to play again? (y/n) ")=='n':
            break


#plane_row()
example_line1=[[0, 0, 5],  [0, [0, 0, 0]], [-1, [0, 0, 1]], [0, [0, 0, 2]], [1, [0, 0, 3]]]
example_line2=[[0, 5, 0], [0, [0, 0, 0]], [0, [0, 1, 0]], [0, [0, 2, 0]], [1, [0, 3, 0]]]
example_line3=[[5, 0, 0], [0, [0, 0, 0]], [0, [1, 0, 0]], [0, [2, 0, 0]], [1, [3, 0, 0]]]
example_line4=[[5, -5, -5], [0, [0, 3, 3]], [0, [1, 2, 2]], [0, [2, 1, 1]], [1, [3, 0, 0]]]
example_line5 = [[0, 5, 0], [-1, [0, 0, 0]], [-1, [0, 1, 0]], [0, [0, 2, 0]], [0, [0, 3, 0]]]
example_grid18 = [[['x', 'x', 'x', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', 'o', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', 'o'], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', 'o']]]
example_grid19 = [[['o', '', '', ''], ['', '', 'o', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', 'x', '', ''], ['', 'x', 'x', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', 'o']]]
row_plane_example_grid = [[['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', 'x', 'x', ''], ['', '', '', ''], ['', '', 'o', ''], ['', 'o', '', '']], [['', 'x', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', 'o']]]
column_plane_example_grid = [[['o', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', 'x', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', 'x', 'o', ''], ['', 'x', 'o', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]]
ex_diag_plane_1 =[[['o', 'o', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', 'x', '', ''], ['', 'x', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', 'x', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', 'o']]]
fuckifIcare = [[['', 'o', '', ''], ['o', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', 'x', '', ''], ['', 'x', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', 'x', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', 'o']]]
ex = [[['', 'o', '', ''], ['', 'x', 'x', 'o'], ['', '', 'x', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', 'o']]]
#print(check_poi(example_line1,example_line3))
#print(example_line1)
#cube_data = get_cube_data(win.example17,'x')
#read_cube_data(cube_data)
#ttt.printGrid(ex)
#cube_data = get_cube_data(example_grid18,'o')
#print(check_threat(cube_data))
#print(block_move(example_line5))
#print(check_row_plane_threat(row_plane_example_grid,'x'))
#print(check_normal_plane_blocked_outside(ex,'x',0))

play_again()

#spectate_again()
#print(change_coordinates([0,0,2]))
input("Press enter to end")