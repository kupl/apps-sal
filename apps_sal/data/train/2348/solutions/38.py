import bisect
n = int(input())
x = list(map(int, input().split()))
l = int(input())
q = int(input())
info = [list(map(int, input().split())) for i in range(q)]
log_table = [[0] * n for i in range(17)]
for i in range(n):
    log_table[0][i] = bisect.bisect_right(x, x[i] + l) - 1
for j in range(1, 17):
    for i in range(n):
        log_table[j][i] = log_table[j - 1][log_table[j - 1][i]]


def solve(_from, to, day):
    pos = _from
    i = 0
    while day:
        if day // 2 > 0:
            if day % 2 == 1:
                pos = log_table[i][pos]
            i += 1
            day = day // 2
        else:
            if day % 2 == 1:
                pos = log_table[i][pos]
            break
    if to <= pos:
        return True
    else:
        return False


for i in range(q):
    ok = n - 1
    ng = 0
    (start, goal) = info[i]
    start -= 1
    goal -= 1
    if start > goal:
        (start, goal) = (goal, start)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(start, goal, mid):
            ok = mid
        else:
            ng = mid
    print(ok)
