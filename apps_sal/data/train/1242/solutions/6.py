t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    s = 0
    while len(a) > 1:
        a.remove(a[1])
        s = s + a[0]
    print(s)
