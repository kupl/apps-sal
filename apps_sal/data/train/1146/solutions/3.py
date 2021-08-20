(N, D) = map(int, input().split())
l = []
for i in range(N):
    l.append(int(input()))
l.sort()
c = 0
while len(l) != 0:
    if len(l) == 1:
        break
    if l[1] - l[0] <= D:
        l.pop(0)
        l.pop(0)
        c += 1
    else:
        l.pop(0)
print(c)
