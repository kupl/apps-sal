from collections import Counter
(n, m) = list(map(int, input().split()))
c = Counter(list(range(1, n + 1)))
s = n * (n + 1) // 2
last = n
first = 1
d = set(list(range(1, n + 1)))
for i in range(m):
    k = int(input())
    if k in d:
        (last, first) = (first, last)
        print(s)
    else:
        s -= last
        d.remove(last)
        d.add(k)
        s += k
        last = k
        print(s)
