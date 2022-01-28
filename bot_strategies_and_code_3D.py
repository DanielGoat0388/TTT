#bot strategies and code
#bot uses CUBE DATA 
import multiplayer_3D as ttt
import collect_cube_data_3D as cube
import itertools 
import random as ran

#____________________________________DEFENSE___________________________________________
#poi of 2 lines defense
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


#simple 3 in a row defense
def block_move(line_): #opponent has three in a row 
    """
    return block move coordinate
    """
    line=line_[:] #remove the line location specification [a,b,c] refer to cube data module
    del line[0]
    for coordinate in line:
        if coordinate[0] != -1:
            return coordinate[1]

def check_3_in_row_threat(cube_data): #check if opponent is about to win
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

#Plane strategy defense
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



#______________________________________________offense moves_________________________________________
def empty_move(line_): #the empty move in a line
    """
    return empty move coordinate
    """
    line=line_[:]
    del line[0]
    for coordinate in line:
        if coordinate[0] != 1: #not already the bot's move
            return coordinate[1]

def check_easy_win_cube(cube_data): #if there is 3 in a row, win
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

def check_bot_2_in_row(cube_data): #threaten to win
    """
    return true if 2 in row, and able to threat
    else, return false and ''
    [boo,coordinate_to_threat]
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


#______________________________________________________________________________________

def change_coordinates(coordinates): #change coordinates from real indices to coordinates
    #print("coordinates " , coordinates)
    for x in range(3):
        coordinates[x]+=1
    return coordinates


def bot_decide_move(grid,bot_symbol,opponent_symbol):
    """
    return best bot_move"""
    cube_data = cube.get_cube_data(grid,bot_symbol) #collect data for lines
        #read_cube_data(cube_data)

    threat2 = check_2_in_line_poi_threat(grid,cube_data) #poi 2 lines
    if threat2[0]: #there is a potential threat
        bot_move = change_coordinates(threat2[1])
    
    threat3 = check_all_plane_threats(grid,opponent_symbol) #center of plane 
    if threat3[0]:#also potentional threat
        bot_move = change_coordinates(threat3[1])

    threat1 = check_3_in_row_threat(cube_data) #3 in a row
    if threat1[0]: #there is immediate threat
        bot_move = threat1[1] #this is the coordinate
                #element+=1#now coordinates should be 1-4
        bot_move = change_coordinates(bot_move)
            #print(bot_move)

    if not threat1[0] and not threat2[0] and not threat3[0]: #there are no threats
        bot_2_in_line = check_bot_2_in_row(cube_data) #check if 2 in a line 
        if bot_2_in_line[0]: #move to threaten player
            #print(bot_symbol , " moved to threat")
            bot_move = change_coordinates(bot_2_in_line[1])


        else:
            while True:
                bot_move = [ran.randint(1,4),ran.randint(1,4),ran.randint(1,4)]
                if ttt.checkMoveNotTake(grid,bot_move):
                    print(bot_symbol , " moved random ")
                    break
        
    easy_3_in_row = check_easy_win_cube(cube_data)
    if easy_3_in_row[0]: #bot can win, this move takes highest precendence
        bot_move = change_coordinates(easy_3_in_row[1])
        print(bot_symbol , " moved to win")
        
    return bot_move


