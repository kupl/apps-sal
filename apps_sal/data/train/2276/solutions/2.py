from sys import stdin


def f(lst, num):
    new = lst[num:] + lst[:num]
    return new


t = int(stdin.readline())
for i in range(t):
    (row, col) = tuple((int(x) for x in stdin.readline().split()))
    lst = list(([int(x)] for x in stdin.readline().split()))
    for j in range(row - 1):
        line = tuple((int(x) for x in stdin.readline().split()))
        for k in range(len(line)):
            lst[k].append(line[k])
    lst.sort(key=lambda x: max(x), reverse=True)
    ans = float('-inf')
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    if col >= 1:
                        aa = f(lst[0], a)
                    else:
                        aa = (0,) * row
                    if col >= 2:
                        bb = f(lst[1], b)
                    else:
                        bb = (0,) * row
                    if col >= 3:
                        cc = f(lst[2], c)
                    else:
                        cc = (0,) * row
                    if col >= 4:
                        dd = f(lst[3], d)
                    else:
                        dd = (0,) * row
                    ans = max(ans, sum((max((x[j] for x in (aa, bb, cc, dd))) for j in range(row))))
    print(ans)
