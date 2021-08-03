
for _ in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))[:a]
    b.sort(reverse=True)
    n1, n2 = 0, 0
    for i in range(a):
        if n1 < n2:
            n1 += b[i]
        else:
            n2 += b[i]
    print(max(n1, n2))
