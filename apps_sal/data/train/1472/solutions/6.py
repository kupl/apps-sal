n = int(input())
(s, p) = (0, 0)
for i in range(10 ** 6):
    x = list(str(i))
    m = 1
    for j in x:
        if m == 0:
            break
        m *= int(j)
    if m == n:
        if '1' in x:
            p += 1
        else:
            s += 1
print(s, p)
