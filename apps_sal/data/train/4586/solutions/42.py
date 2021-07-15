remote_grid = [
['a','b','c','d','e','1','2','3'],
['f','g','h','i','j','4','5','6'],
['k','l','m','n','o','7','8','9'],
['p','q','r','s','t','.','@','0'],
['u','v','w','x','y','z','_','/'],
]
rem_x = 8
rem_y = 5
remote_map = {}
for y in range(rem_y):
    for x in range(rem_x):
        remote_map[ remote_grid[y][x] ] = (x,y)
def tv_remote(word):    
    currpos = (0,0)
    clicks = 0
    for c in word:
        nextpos = remote_map[c]
        clicks += abs(nextpos[0]-currpos[0]) + abs(nextpos[1]-currpos[1])
        currpos = nextpos
    return clicks+len(word)

