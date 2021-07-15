l = []
for _ in range(int(input())):
    l.append(int(input()))

ran = max(l)

s = set()
out = []
for i in range(2,ran+1):
    s.clear()
    for j in l:
        s.add(j%i)
    if len(s) == 1:
        out.append(i)

out.sort()

print(*out)

