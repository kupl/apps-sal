import math
import sys
n = int(sys.stdin.readline().strip())
for i in range(n):
    n = int(sys.stdin.readline().strip())
    mx = -math.inf
    px = math.inf
    my = -math.inf
    py = math.inf
    robots = [list(map(int, sys.stdin.readline().split())) for x in range(n)]
    for robot in robots:
        if robot[2] == 0:
            mx = max(robot[0], mx)
        if robot[5] == 0:
            my = max(robot[1], my)
        if robot[4] == 0:
            px = min(robot[0], px)
        if robot[3] == 0:
            py = min(robot[1], py)
    if mx > px or my > py:
        print(0)
    else:
        print(1, max(-100000, mx), max(-100000, my))
