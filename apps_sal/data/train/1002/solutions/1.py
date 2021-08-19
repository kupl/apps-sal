T = int(input())
for i in range(0, T):
    (N, D) = list(map(int, input().split()))
    s = [int(x) for x in input().split()]
    L = []
    for j in range(0, len(s)):
        L.append(j)
    arr = sorted(zip(s, L))
    ptr = -1
    for j in range(0, len(arr)):
        if arr[j][1] == 0:
            ptr = j
            break
    if N == 1:
        print('YES')
    else:
        temp1 = 0
        temp2 = 0
        temp = 0
        for j in range(0, len(arr) - 1):
            if abs(arr[j][0] - arr[j + 1][0]) > D:
                temp = 1
                break
        if ptr != 0 and ptr != len(arr) - 1:
            for j in range(0, ptr):
                if abs(arr[j][0] - arr[j + 2][0]) > D:
                    temp1 = 1
                    break
            if temp1 == 1:
                for j in range(ptr - 1, len(arr) - 2):
                    if abs(arr[j][0] - arr[j + 2][0]) > D:
                        temp2 = 1
                        break
        if temp == 0 and (temp1 == 0 or temp2 == 0):
            print('YES')
        else:
            print('NO')
