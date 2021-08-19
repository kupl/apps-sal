t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    s = 0
    for i in l:
        if i % 6 == 0:
            s += 6
        else:
            s += i % 6
    print(s)
