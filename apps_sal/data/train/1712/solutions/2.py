def puzzle_solver(pieces, width, height):
    solution,corner,d3={},{},{}
    for y in range(height+1):corner[0,y]=None
    for x in range(width+1): corner[x,0]=None
    for (a,b),(c,d),e in pieces:d3[a,b,c]=(d,e)
    for y in range(height):
        for x in range(width):
            corner[x+1,y+1],solution[x,y]=d3[corner[x,y],corner[x+1,y],corner[x,y+1]]
    return [tuple(solution[x,y] for x in range(width)) for y in range(height)]
