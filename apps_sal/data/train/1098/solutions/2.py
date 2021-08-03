t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    a.sort(reverse=True)
    for i in range(0, len(a), 2):
        c += a[i]
    print(c)
    t -= 1
