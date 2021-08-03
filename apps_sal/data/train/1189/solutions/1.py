from collections import Counter


def result(a, n):

    ans = 0
    total = sum(a)
    prefix = 0
    d = Counter()
    for i in range(n):
        remains = total - a[i]
        if not remains % 2:
            ans += d[remains // 2]
        prefix += a[i]
        d[prefix] += 1
    d.clear()
    suffix = 0
    for i in range(n - 1, -1, -1):
        remains = total - a[i]
        if not remains % 2:
            ans += d[remains // 2]
        suffix += a[i]
        d[suffix] += 1
    return ans


queries = []
for _ in range(int(input())):
    n = input()
    queries.append(list(map(int, input().split())))
for q in queries:
    print(result(q, len(q)))
