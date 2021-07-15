def distribution_of(golds):
    g = golds[:]
    total = [0,0]
    turn = 0
    while len(g) > 0:
        if g[0] >= g[-1]:
            value = g.pop(0)
        else:
            value = g.pop(-1)      
        total[turn % 2] += value    
        turn += 1
    return total
