(a, b) = list(map(int, input().split()))
c = []
(d, e) = (1, b + 1)
while e > d:
    c += [d, e]
    e -= 1
    d += 1
if e == d:
    c.append(e)
print(' '.join(map(str, c + list(range(b + 2, a + 1)))))
