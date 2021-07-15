def pack_bagpack(scores,weights,capacity):
    sols=[[0 for j in range(capacity+1)] for i in range(len(scores)+1)]
    scores.insert(0, 0)
    weights.insert(0, 0)
    for y,iy in enumerate(sols[1:],1):
        for x,ix in enumerate(iy[1:],1):
            if weights[y]<=x:
                sols[y][x]=max(scores[y]+sols[y-1][x-weights[y]],sols[y-1][x])
            else:
                sols[y][x]=sols[y-1][x]
    return sols[-1][-1]
