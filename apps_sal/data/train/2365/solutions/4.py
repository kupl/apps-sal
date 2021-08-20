from collections import Counter
from itertools import chain


def dfs(n, r, hint_sets, count, removed, result):
    if len(result) == n - 1:
        last = (set(range(1, n + 1)) - set(result)).pop()
        result.append(last)
        return True
    (i, including_r) = (0, None)
    for (i, including_r) in enumerate(hint_sets):
        if i in removed:
            continue
        if r in including_r:
            break
    removed.add(i)
    next_r = []
    for q in including_r:
        count[q] -= 1
        if count[q] == 1:
            next_r.append(q)
    if not next_r:
        return False
    if len(next_r) == 2:
        nr = -1
        (can1, can2) = next_r
        for (i, h) in enumerate(hint_sets):
            if i not in removed:
                continue
            if can1 in h and can2 not in h:
                nr = can1
                break
            if can1 not in h and can2 in h:
                nr = can2
                break
        if nr == -1:
            nr = can1
    else:
        nr = next_r[0]
    result.append(nr)
    res = dfs(n, nr, hint_sets, count, removed, result)
    if res:
        return True
    result.pop()
    for q in including_r:
        count[q] += 1
    return False


t = int(input())
buf = []
for l in range(t):
    n = int(input())
    hints = []
    for _ in range(n - 1):
        (k, *ppp) = list(map(int, input().split()))
        hints.append(ppp)
    count = Counter(chain.from_iterable(hints))
    most_common = count.most_common()
    hint_sets = list(map(set, hints))
    r = most_common[-1][0]
    result = [r]
    if dfs(n, r, hint_sets, dict(count), set(), result):
        buf.append(' '.join(map(str, result[::-1])))
        continue
    r = most_common[-2][0]
    result = [r]
    assert dfs(n, r, hint_sets, dict(count), set(), result)
    buf.append(' '.join(map(str, result[::-1])))
print('\n'.join(map(str, buf)))
