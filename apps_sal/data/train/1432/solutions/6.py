for __ in range(int(input())):
    a = []
    n = int(input())
    for i in range(n):
        a.append(list(map(int, input().split())))
    count = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                count += 1
    temp = n - 1
    for k in range(n - 1):
        arb = int((n - 1 - k) * (n - k))
        if count >= arb:
            temp = k
            break
    print(temp)
