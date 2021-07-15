# number the cube faces like a dice 1-6
def folding(grid,face,list_on_face,remain_list):
    faces=[face]
    dirs=[1,-1,5,-5]
    if list_on_face % 5==1:
        dirs.remove(-1)
    if list_on_face % 5 ==0:
        dirs.remove(1)
    goto_dirs=[]
    print(remain_list)
    for direction in dirs:
        goto_cell=direction+list_on_face
        print((goto_cell,remain_list))
        if goto_cell in remain_list:
            remain_list.remove(goto_cell)
            goto_dirs.append(direction)
    print(("face",face,"grid",grid,"listCELL",list_on_face,"to",goto_dirs))
    for direction in goto_dirs:
        faces.extend(folding(
            grid=new_grid(face,direction,grid),
            face=new_face(grid, direction),
            list_on_face=list_on_face+direction,
            remain_list=remain_list
        ))
    return faces

def new_face(grid,direction):
    return grid[[1,-1,5,-5].index(direction)]

def new_grid(face, direction, grid):
    opposite_face={1:6,2:4,6:1,4:2,5:3,3:5}
    dir_index={1:0,-1:1,5:2,-5:3}
    newgrid=grid.copy()
    newgrid[dir_index[-direction]]=face
    newgrid[dir_index[direction]]=opposite_face[face]
    return newgrid

def fold_cube(number_list):
    faces=folding(grid=[3,5,2,4], #in dir [1,-1,5,-5]
            face=1,
            list_on_face=number_list[0],
            remain_list=number_list[1:])
    return sorted(faces)==list(range(1,7))
    #return True or False

