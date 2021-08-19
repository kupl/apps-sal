t = int(input())
for i in range(t):
    nk = list(map(int, input().split()))
    n = nk[0]
    k = nk[1]
    arr = list(map(int, input().split()))
    a1 = []
    a2 = []
    for i in range(0, len(arr)):
        if i % 2 == 0:
            a1.append(arr[i])
        else:
            a2.append(arr[i])
    if sum(a1) >= sum(a2):
        a1.sort()
        a2.sort()
        for j in range(k):
            if j < len(a1) and j < len(a2):
                temp = a1[len(a1) - j - 1]
                a1[len(a1) - j - 1] = a2[j]
                a2[j] = temp
    if sum(a1) >= sum(a2):
        print('NO')
    else:
        print('YES')
