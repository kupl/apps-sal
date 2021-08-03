t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    c = a[k - 1]
    a.sort()
    for i in range(n):
        if a[i] == c:
            print(i + 1)
            break
