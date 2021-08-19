try:
    (N, D) = map(int, input().split())
    space = []
    for __ in range(N):
        space.append(int(input()))
    space.sort()
    i = 0
    score = 0
    j = 1
    while i < len(space):
        if i < len(space) - 1 and j < len(space):
            a = space[i]
            b = space[j]
            if b - a <= D:
                i += 2
                j += 2
                score += 1
            else:
                i += 1
                j += 1
        else:
            break
    print(score)
except:
    pass
