n, p = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
c = 0
s = 0
for i in l:
    s += i
    if s > p:
        break
    else:
        c += 1
print(c)
