for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    rating = list(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    minrank = [float('inf')] * n
    index2 = [0] * n
    bestscore = [float('-inf')] * n
    index1 = [0] * n
    for i in range(m):
        for j in range(n):
            rating[j] += arr[j][i]
        st = sorted(rating, reverse=True)
        f = []
        dindex = dict()
        for j in range(len(st)):
            if st[j] in dindex:
                continue
            dindex[st[j]] = j
        for j in range(len(rating)):
            f.append(dindex[rating[j]])
        for ii in range(len(f)):
            if minrank[ii] > f[ii]:
                minrank[ii] = f[ii]
                index1[ii] = i
        for ii in range(len(rating)):
            if bestscore[ii] < rating[ii]:
                bestscore[ii] = rating[ii]
                index2[ii] = i
    count = 0
    for (i, j) in zip(index2, index1):
        if i != j:
            count += 1
    print(count)
