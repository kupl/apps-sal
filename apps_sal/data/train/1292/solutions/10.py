arr = list(map(int, input().split()))

n = arr.pop(0)
m = arr.pop(0)
w = arr.pop(0)
b = arr.pop(0)

whites = {}
for i in range(0, 2 * w - 1, 2):
    x = arr[i] - 1
    y = arr[i + 1] - 1

    if x in whites:
        whites[x].append(y)
    else:
        whites[x] = [y]

blacks = {}
for i in range(2 * w, 2 * (w + b), 2):
    x = arr[i] - 1
    y = arr[i + 1] - 1

    if x in blacks:
        blacks[x].append(y)
    else:
        blacks[x] = [y]


def simulateRay(x, y):
    wRow = {}
    bRow = {}

    if x in whites:
        wRow = whites[x]

    if x in blacks:
        bRow = blacks[x]
    else:
        if (len(wRow) == 0) or ((len(wRow) == 1) and (wRow[0] != y)):
            return m - y

    if (y in wRow) or (y in bRow):
        return 0

    wCount = 0

    l = 1
    while y < (m - 1):

        if y in wRow:
            wCount += 1
            if wCount == 2:
                return l
        if y in bRow:
            return l

        l += 1
        y += 1

    return l


total = 0
allL = m * (m + 1) / 2
for i in range(n):
    for j in range(m):
        res = simulateRay(i, j)
# print(i,j,res)
        total += res

print(total)
