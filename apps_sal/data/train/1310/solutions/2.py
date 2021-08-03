t = eval(input())
while t > 0:
    p = input()
    count = 0
    cost = 0
    i = 0
    while i < len(p):
        if count == 6:
            count = 0
            i = i + 1
            continue
        if p[i] == 'M':
            cost = cost + 3
        else:
            cost = cost + 4
        count = count + 1
        i = i + 1
    print(cost)
    t = t - 1
