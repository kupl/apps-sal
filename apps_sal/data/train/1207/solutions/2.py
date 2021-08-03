# cook your dish here
for _ in range(int(input())):
    n = int(input())
    m = 1000001
    s = 0
    for x in map(int, input().split()):
        m = min(m, x)
        s += x
    s -= m
    s *= m
    print(s)
