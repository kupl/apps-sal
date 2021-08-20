for i in range(int(input())):
    l = [int(j) for j in input().split()]
    (n, m) = (l[0], l[1])
    idx = 0
    count = 0
    arr = []
    for j in range(m, n):
        arr.append(j + 1)
    for j in range(m):
        arr.append(j + 1)
    for j in range(n):
        idx = arr[idx] - 1
        count += 1
        if idx == 0:
            break
    if count == n:
        print('Yes')
    else:
        print('No ' + str(count))
