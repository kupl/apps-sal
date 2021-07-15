def solomons_quest(arr):
    l,c = 0,[0,0]
    for way in arr:
        l+=way[0]
        c[(way[1]+1)%2] += ((-1)**(way[1]//2)) *way[2]*(2**l)
    return c
