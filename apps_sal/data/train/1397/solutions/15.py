for T in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    d = {}
    elements = []
    for i in range(N):
        if a[i] not in d:
            d[a[i]] = [i]
            elements.append(a[i])
        else:
            d[a[i]].append(i)
    elements.sort()
    M = 1
    prev_index = d[elements[0]][0]
    for i in range(1, len(elements)):
        flag = True
        for j in range(len(d[elements[i]])):
            if prev_index < d[elements[i]][j]:
                flag = False
                prev_index = d[elements[i]][j]
                break
        if flag:
            M += 1
            prev_index = d[elements[i]][0]
    print(M)
