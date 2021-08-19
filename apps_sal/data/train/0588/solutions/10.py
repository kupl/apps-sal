t = int(input())
for x in range(t):
    cu = int(input())
    angle = list(map(int, input().split()))
    diff = []
    mi = float('infinity')
    for i in range(cu - 1):
        diff.append(angle[i + 1] - angle[i])
        if diff[i] < mi:
            mi = diff[i]
    diff.append(angle[0] - angle[cu - 1] + 360)
    if diff[cu - 1] < mi:
        mi = diff[cu - 1]
    div = 1
    while div < 360:
        smallest = mi / div
        count = 0
        flag = True
        for i in diff:
            dm = divmod(i, smallest)
            if dm[1] != 0:
                flag = False
                break
            count += dm[0]
        if flag:
            print(int(count - cu))
            break
        div += 1
