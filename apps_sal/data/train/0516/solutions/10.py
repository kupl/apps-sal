for i in range(int(input())):
    n, k = map(int, input().split())
    s, a, l = 0, 0, list(map(int, input().split()))
    l2 = 2 * l
    for i in range(n - 1):
        for j in range(i + 1, n):
            if(l[i] > l[j]):
                a += 1
    for i in range(n):
        for j in range(n, 2 * n):
            if(l2[i] > l2[j]):
                s += 1
    print(((k * (k - 1)) // 2) * s + k * a)
