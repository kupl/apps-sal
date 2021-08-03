from collections import defaultdict


def digitSum(n):
    n = str(n)
    s = 0
    for i in range(len(n)):
        s += int(n[i])
    return s


def solve(n, d):
    queue = [[n, 0]]
    has = defaultdict(int)
    i = 0
    while i < 10000 and len(queue) != 0:
        t = queue.pop(0)
        if t[0] < 10:
            if t[0] not in has:
                has[t[0]] = t[1]
        else:
            queue.append([digitSum(t[0]), t[1] + 1])
        queue.append([t[0] + d, t[1] + 1])
        i += 1
    print(min(has), has[min(has)])


for _ in range(int(input())):
    n, d = map(int, input().split())
    solve(n, d)
