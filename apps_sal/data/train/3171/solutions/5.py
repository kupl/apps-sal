def crashing_weights(a):
    li = [list(i) for i in zip(*a)]
    for i in range(len(li)):
        for j in range(len(li[i]) - 1):
            if li[i][j] > li[i][j + 1]:
                li[i][j + 1] += li[i][j]
                li[i][j] = 0
    return [list(i) for i in zip(*li)][-1]
