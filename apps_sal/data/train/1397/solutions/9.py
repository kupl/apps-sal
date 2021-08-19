from sys import stdin
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    final = {}
    m = sorted(list(set(arr)))
    count = 0
    d = {}
    for i in range(n):
        if arr[i] in d:
            d[arr[i]].append(i)
        else:
            d[arr[i]] = [i]
    pos = d[m[0]][0]
    j = 1
    while j < len(m):
        k = None
        for item in d[m[j]]:
            if item > pos:
                k = item
                break
        if k != None:
            j += 1
            pos = k
        else:
            count += 1
            pos = -1
    print(count + 1)
