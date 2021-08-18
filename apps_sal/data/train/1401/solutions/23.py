n, a = map(int, input().split())
l = [int(x) for x in input().split()]
l.sort()
c = 0
while(a > l[c]):
    a = a - l[c]
    c += 1
print(c)
