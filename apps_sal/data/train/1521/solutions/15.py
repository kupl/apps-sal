def winner(x, y):
    if x[0] < y[0]:
        if x[1] >= y[1]:
            return 1
        else:
            return 0
    elif x[1] > y[1]:
        if x[0] <= y[0]:
            return 1
        else:
            return 0
    elif x[1] < y[1]:
        if x[0] >= y[0]:
            return 2
        else:
            return 0
    elif x[0] > y[0]:
        if x[1] <= y[1]:
            return 2
        else:
            return 0
    else:
        return 0


for _ in range(int(input())):
    n = int(input())
    part = []
    for _ in range(n):
        part.append(tuple(map(int, input().split())))
    score = [0] * n
    for i in range(n):
        x = part[i]
        if i < n - 1:
            new = part[i + 1:]
            for y in range(len(new)):
                if winner(x, new[y]) == 0:
                    score[i] += 1
                    score[i + y + 1] += 1
                elif winner(x, new[y]) == 1:
                    score[i] += 2
                else:
                    score[i + y + 1] += 2
    print(*score)
