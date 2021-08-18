t = int(input())
for _ in range(t):
    scores = []

    n = int(input())
    for i in range(n):
        items = list(map(int, input().split()))
        p = items[0]

        iscore = 0
        m = [[] for j in range(p)]
        for k in range(p):
            for l in range(p):
                if items[k + 1] not in m[l]:

                    m[l].append(items[k + 1])
                    break
        for k in range(len(m)):
            if len(m[k]) == 4:
                iscore += (4 + 1)
            elif len(m[k]) == 5:
                iscore += (5 + 2)
            elif len(m[k]) == 6:
                iscore += (6 + 4)
            else:
                iscore += len(m[k])
        scores.append(iscore)
    f = scores.index(max(scores))
    if scores.count(max(scores)) > 1:
        print("tie")
    elif f == 0:
        print("chef")
    else:
        print(f + 1)
