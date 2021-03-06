import numpy as np


def count(gamefield, PM, N):
    gamefield[PM[0], PM[1]] = -1
    case1 = 0
    case2 = 0
    case3 = 0
    case4 = 0
    if PM[0] + 1 < N and gamefield[PM[0] + 1, PM[1]] != -1:
        case1 = 1 + count(gamefield, [PM[0] + 1, PM[1]], N)
    if PM[0] - 1 > -1 and gamefield[PM[0] - 1, PM[1]] != -1:
        case2 = 1 + count(gamefield, [PM[0] - 1, PM[1]], N)
    if PM[1] + 1 < N and gamefield[PM[0], PM[1] + 1] != -1:
        case3 = 1 + count(gamefield, [PM[0], PM[1] + 1], N)
    if PM[1] - 1 > -1 and gamefield[PM[0], PM[1] - 1] != -1:
        case4 = 1 + count(gamefield, [PM[0], PM[1] - 1], N)
    return case1 + case2 + case3 + case4


def pac_man(N, PM, enemies):
    if N == 1:
        return 0
    if len(enemies) == 0:
        return N ** 2 - 1
    gamefield = np.ones((N, N))
    gamefield[PM[0], PM[1]] = 7
    for e in enemies:
        gamefield[:, e[1]] = -1
        gamefield[e[0], :] = -1
    print(gamefield)
    return count(gamefield, PM, N)
