def how_many_bees(hive):
    if not hive: return 0
    hive = [list(x) for x in hive]
    directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
    output = 0
    for row, _ in enumerate(hive):
        for col, val in enumerate(_):
            curr = 'b'
            if val == 'b':
                for direction in directions:
                    coord = (row+direction[0], col+direction[1])
                    if inBounds(hive, coord) and hive[coord[0]][coord[1]] == 'e':
                        output += traverse(hive, coord, direction, curr)
    return output                       

def traverse(hive, coord, direction, curr):

    curr += hive[coord[0]][coord[1]]
    new_c = (coord[0]+direction[0], coord[1]+direction[1])

    if curr == 'bee':
        return 1
    if(inBounds(hive, new_c)):
        return traverse(hive, new_c, direction, curr)   
    return 0
        
    
def inBounds(hive, coord):
    row, col = len(hive), len(hive[0])
    if 0 <= coord[0] < row and 0 <= coord[1] < col:
        return True
    return False
