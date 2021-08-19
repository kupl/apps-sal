for i in range(int(input())):
    (n, k) = list(map(int, input().split()))
    dict1 = {}
    for j in range(n):
        (s, e, p) = list(map(int, input().split()))
        try:
            dict1[p].append((e, s))
        except:
            dict1[p] = [(e, s)]
    count = 0
    for k in dict1:
        dict1[k].sort()
        start = -1
        for j in dict1[k]:
            if j[1] >= start:
                start = j[0]
                count += 1
    print(count)
