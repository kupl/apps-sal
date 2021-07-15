def solve(emulator):
    num_drops = emulator.drops
    num_eggs = emulator.eggs
    #generate table for max heights with certain numbers of eggs and drops
    HEIGHTS = heights(num_eggs, num_drops)
    return solve_part(emulator, 0, HEIGHTS[num_eggs][num_drops], HEIGHTS)+1
    
    
def solve_part(emulator, min_floor, max_floor, HEIGHTS):
    #solve for the highest possible floor without breaking
    if min_floor == max_floor:
        return min_floor
    else:
        num_drops = emulator.drops
        num_eggs = emulator.eggs
        partition = HEIGHTS[num_eggs-1][num_drops-1]
        partition_point = min_floor + partition + 1
        if emulator.drop(partition_point):
            return solve_part(emulator, min_floor, partition_point-1, HEIGHTS)
        else:
            return solve_part(emulator, partition_point, max_floor, HEIGHTS)
        
def heights(n, m):
    heights = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            heights[i][j] = heights[i-1][j-1] + heights[i][j-1] + 1
    return heights



