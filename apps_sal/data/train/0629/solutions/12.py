T = int(input())
for i in range(T):
    [r, g, b, k] = list(map(int, input().split()))
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    c = list(map(int, input().split()))
    j = sorted([max(s), max(t), max(c)])
    for i in range(k):
        j[-1] = int(j[-1] / 2)
        j = sorted(j)
    print(j[-1])
