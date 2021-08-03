for u in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    d = []
    for i in range(n):
        for j in range(i + 1, n):
            d.append(abs(l[i] + l[j] - k))
    print(min(d), d.count(min(d)))
