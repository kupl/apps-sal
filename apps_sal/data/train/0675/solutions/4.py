t = int(input())
for i in range(t):
    n = int(input())
    if n == 1:
        print(1)
    elif n & n - 1 == 0:
        print(-1)
    else:
        v = [2, 3, 1]
        for i in range(4, n + 1):
            v.append(i)
        for i in range(3, n):
            if v[i] & v[i - 1] == 0:
                (v[i], v[i + 1]) = (v[i + 1], v[i])
        for i in range(len(v)):
            print(v[i], end=' ')
        print()
