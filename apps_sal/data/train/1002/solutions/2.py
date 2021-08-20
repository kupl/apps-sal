tests = int(input())
for te in range(tests):
    (n, d) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    c = arr[0]
    arr.sort()
    for i in range(n):
        if arr[i] == c:
            index = i
    flag = 0
    for i in range(1, n):
        if abs(arr[i] - arr[i - 1]) > d:
            print('NO')
            flag = 1
            break
    if flag == 1:
        continue
    if index == 0 or index == n - 1:
        print('YES')
        continue
    for i in range(index + 1, n):
        if abs(arr[i] - arr[i - 2]) > d:
            flag = 1
            break
    if flag == 0:
        print('YES')
        continue
    flag = 0
    for i in range(index - 1, -1, -1):
        if abs(arr[i] - arr[i + 2]) > d:
            flag = 1
            break
    if flag == 0:
        print('YES')
        continue
    else:
        print('NO')
