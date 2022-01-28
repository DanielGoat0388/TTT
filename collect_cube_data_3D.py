#Collect cube data for 3D bot ttt
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
