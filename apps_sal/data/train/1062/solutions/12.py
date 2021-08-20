n = int(input())
l = [[1]]
if n == 1:
    pass
else:
    i = 2
    while i <= n:
        l1 = [i for j in range(2 * i - 3)]
        l.insert(0, l1)
        for j in l:
            j.append(i)
            j.insert(0, i)
        i += 1
for i in l:
    print(*i)
for i in range(len(l) - 2, -1, -1):
    print(*l[i])
