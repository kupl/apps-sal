n = int(input())
(c1, c2) = (0, 0)
for i in range(1000001):
    j = i
    p = 1
    f = 0
    while j > 0:
        p *= j % 10
        if j % 10 == 1:
            f = 1
        j = j // 10
    if p == n:
        if f == 0:
            c1 += 1
        else:
            c2 += 1
print(c1, c2)
