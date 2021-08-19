t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    print(l[-1] * l[-2], end=' ')
    print(l[0] * l[1])
