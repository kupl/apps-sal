for i in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = [1]
    p = 1
    ne = 0
    m = 0
    for j in range(2, n + 1):
        if j % 2 == 0:
            if p != k:
                arr.append(j)
                p += 1
            else:
                m = 1
                break
        else:
            if ne != (n - k):
                arr.append(-j)
                ne += 1
            else:
                m = -1
                break

    if abs(arr[-1]) != n and m == -1:
        for x in range(arr[-1] + 1, n + 1):
            arr.append(x)
    elif abs(arr[-1]) != n and m == 1:

        for x in range(abs(arr[-1]) + 1, n + 1):

            arr.append(-x)
    print(*arr)
