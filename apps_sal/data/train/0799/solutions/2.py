T = int(input())
c = 0
while T:
    l = [int(k) for k in input().split()]
    a = l.count(1)
    if a >= 2:
        c += 1
    T -= 1
print(c)
