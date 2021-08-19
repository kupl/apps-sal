(n, m) = map(int, input().split())
b = [[int(x) for x in list(input())] for x in range(n)]
c = int(input())
size = min(n, m)
res = [size ** 2 for x in range(size + 1)]


def invert(i, j, r, ele):
    count = 0
    for (index, x) in enumerate(range(i, i + r)):
        temp = ele
        if index % 2:
            temp = 0 if ele else 1
        for y in range(j, j + r):
            count += 0 if temp == b[x][y] else 1
            temp = 0 if temp else 1
    return count


for s in range(size, 1, -1):
    flag = 0
    for x in range(n - s + 1):
        for y in range(m - s + 1):
            ic = min(invert(x, y, s, 0), invert(x, y, s, 1))
            res[s] = min(res[s], ic)
            if not ic:
                flag = 1
                break
        if flag:
            break
    if flag:
        break
for t in map(int, input().split()):
    for (index, e) in reversed(list(enumerate(res))):
        if e <= t:
            print(index)
            break
res = list(map(lambda x: 0 if x == size ** 2 else x, res))
