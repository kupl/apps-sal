from math import *

def horizontal_yield(x, point, end):
    length = hypot(point[0]-x, point[1]-50)
    distance = 2*(point[0]-x)
    if distance > end - x: distance = end - x
    return distance / length if point[1] - length >= 20 else 0

def optimal_latch(ar, x):
    x_opt = 0
    yield_opt = 0
    for building in ar:        
        if building[1] + building[2] < x: continue
        x_max = x + int(sqrt((building[0]-20)**2-(building[0]-50)**2))
        if x_max < building[2]: continue
        if 2 * x_max - x > ar[-1][1] + ar[-1][2]:
            x_max = max(building[2], int(ceil((ar[-1][1] + ar[-1][2] + x) / 2)))
        x_max = min(x_max, building[1] + building[2])
        yield_x = horizontal_yield(x, [x_max, building[0]], ar[-1][1] + ar[-1][2])
        if yield_x > yield_opt or (2 * x_max - x >= ar[-1][1] + ar[-1][2] and 2 * x_opt - x < ar[-1][1] + ar[-1][2]):
            yield_opt = yield_x
            x_opt = x_max
    return int(x_opt)
        

def spidey_swings(ar):
    print(ar)
    spidey_x = 0
    latches = []
    for i in range(len(ar)):
        ar[i].append(0 if i==0 else ar[i-1][1] + ar[i-1][2])
    while spidey_x < ar[-1][1] + ar[-1][2]:
        latches.append(optimal_latch(ar,spidey_x))   
        spidey_x = 2 * latches[-1] - spidey_x
    return latches
