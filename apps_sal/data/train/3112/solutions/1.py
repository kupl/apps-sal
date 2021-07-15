def avoid_obstacles(a):
    for j in range(2, max(a) + 2):        
        if all(e % j != 0 for e in a): return j
