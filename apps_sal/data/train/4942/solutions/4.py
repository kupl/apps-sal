def directions(goal):
    MOVES = {'N': [0,1], 'S': [0,-1], 'E': [1,1], 'W': [1,-1]}
    g = [0,0]
    for d in goal: g[MOVES[d][0]] += MOVES[d][1]
    return ["SN"[g[0]>=0]] * abs(g[0]) + ["WE"[g[1]>=0]] * abs(g[1])
