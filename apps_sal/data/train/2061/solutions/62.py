T = int(input())
A = []


def direction(inp):
    if inp.count(min(inp)) == 1:
        return 1
    else:
        return 0


for i in range(T):
    (x1, y1, x2, y2, x3, y3) = map(int, input().split())
    x = [x1, x2, x3]
    y = [y1, y2, y3]
    dst = [min(x) * 2 + direction(x), min(y) * 2 + direction(y)]
    step = max(abs(dst[0]), abs(dst[1]))
    if dst == [0, 0]:
        step = 0
    elif dst == [1, 1]:
        step = 1
    elif dst[0] == dst[1]:
        step += 1
    A += [step]
for i in A:
    print(str(i))
