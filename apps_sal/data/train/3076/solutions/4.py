def solve(arr):
    route = [road.split() for road in arr]
    (l, re) = (len(arr), [])
    dir = {'Left': 'Right', 'Right': 'Left', 'Begin': 'Begin'}
    for i in range(l):
        re.insert(0, ' '.join([dir[route[(i + 1) % l][0]]] + route[i][1:]))
    return re
