t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for x in a:
        s += x % 6
        if x % 6 == 0:
            s += 6
    print(s)
