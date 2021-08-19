for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = set()
    c = []
    for i in a:
        if i in b:
            c.append(i)
        else:
            b.add(i)
    b = list(b)
    b.sort()
    c.sort(reverse=True)
    arr = b[:] + c[:]
    flag = 0
    for i in range(len(b) - 1, n - 1):
        if arr[i] == arr[i + 1]:
            flag = 1
            print('NO')
            break
    if flag == 0:
        print('YES')
        print(*arr)
