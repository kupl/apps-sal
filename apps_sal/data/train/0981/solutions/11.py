t = eval(input())
for i in range(t):
    n = eval(input())
    l = list(map(int, input().split()))
    d = []
    l.sort()
    for i in range(1, n):
        d.append(l[i] - l[i - 1])
    print(min(d))
