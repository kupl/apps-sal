m = int(input())
a, b, start, end = [], [], 0, 0

idx = 0

for _ in range(m):
    line = list(map(int, input().split()))
    if line[0] == 1:
        x = line[1]
        start = end + 1
        end = end + 1
        if len(a) <= 100000:
            a.append(x)
        b.append((start, end, x))
    else:
        l, c = line[1], line[2]
        start = end + 1
        end = end + l * c
        if len(a) <= 100000:
            for _ in range(c):
                a += a[:l]
                if len(a) > 100000:
                    break
        b.append((start, end, l, c))


input()  # n


def answer(n):
    nonlocal m, a, b, idx

    if (n - 1) < len(a):
        return a[n - 1]

    while True:
        bi = b[idx]
        if bi[0] <= n <= bi[1]:
            break
        idx += 1

    if len(bi) == 3:
        return bi[2]

    n_bak = n
    n = (n - bi[0]) % bi[2] + 1

    return a[n - 1]


result = []
for n in map(int, input().split()):
    result.append("%s" % answer(n))

print(" ".join(result))

