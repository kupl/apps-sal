n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
l.sort()
l.reverse()
i = 0
count = 0
while i < len(l):
    s = l[i]
    l1 = l[i + 1:len(l)]
    if len(l1) != 0 and s >= 2 * l1[len(l1) - 1]:
        for j in l1:
            if s >= 2 * j:
                l.remove(j)
                break
    count += 1
    i += 1
print(count)
