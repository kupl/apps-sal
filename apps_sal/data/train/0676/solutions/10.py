from collections import Counter


def count(s):
    c = Counter(s)
    return c.most_common(1)[0][0]


t = int(input())
for i in range(t):
    n = int(input())
    s = sorted(list(map(str, input().split())))
    print(count(s))
