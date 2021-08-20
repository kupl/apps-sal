n = int(input())


def digits(v):
    s = 0
    while v > 0:
        s += v % 10
        v //= 10
    return s


a = []
for x in range(max(0, n - 81), n):
    if x + digits(x) == n:
        a.append(x)
print(len(a))
if len(a) > 0:
    print(' '.join(map(str, a)))
