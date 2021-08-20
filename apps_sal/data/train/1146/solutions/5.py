(n, d) = list(map(int, input().split()))
l = list()
pair = 0
for _ in range(n):
    l.append(int(input()))
l.sort()
while len(l) != 0:
    if len(l) == 1:
        break
    if abs(l[0] - l[1]) <= d:
        pair += 1
        l.pop(0)
        l.pop(0)
    else:
        l.pop(0)
print(pair)
