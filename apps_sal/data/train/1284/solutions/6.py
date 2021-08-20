for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(' ')))
    a.sort(reverse=True)
    x = n // 4 - 1
    y = x + n // 4
    z = y + n // 4
    if a[x] == a[x + 1]:
        print(-1)
        continue
    if a[y] == a[y + 1]:
        print(-1)
        continue
    if a[z] == a[z + 1]:
        print(-1)
        continue
    print(a[z], a[y], a[x])
