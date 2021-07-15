def tower_of_hanoi(rings):
    count = 7
    for i in range(4,rings+1):
        count = count*2 + 1
        
    return count
