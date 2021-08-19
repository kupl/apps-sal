x = int(input())
y = list(map(int, input().strip().split(' ')))
(d, pd, l, pl) = (0, 0, 0, 0)
(md, ml) = (0, 0)
for i in range(0, x):
    if y[i] == 1:
        d = d + 1
        if d > md:
            (md, pd) = (d, i + 1)
    if y[i] == 2:
        d = d - 1
    if d != 0:
        l = l + 1
        if l > ml:
            (ml, pl) = (l, i - l + 1)
    else:
        l = 0
print(md, pd, ml + 1, pl + 1)
