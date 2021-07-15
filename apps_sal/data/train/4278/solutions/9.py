def diagonal(l):
    a,b = zip(*[(l[i][-i-1], l[i][i]) for i in range(len(l))])
    
    if sum(a) < sum(b):
        return "Principal Diagonal win!"
    elif sum(a) > sum(b):
        return "Secondary Diagonal win!"
    return 'Draw!'
