n, m = map(int, input().split())
t = n + m
l = []
while t > 0:
    a = int(input())
    if a != -1:
        l.append(a)
    else:
        l.sort()
        print(l[-1])
        l[-1] = 0
    t = t - 1
