from itertools import accumulate
(n, m, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
oper = [tuple(map(int, input().split())) for i in range(m)]
zapr = [tuple(map(int, input().split())) for i in range(k)]
count_ = [0 for i in range(m + 1)]
for el in zapr:
    (x, y) = el
    count_[x - 1] += 1
    count_[y] -= 1
counter_ = list(accumulate(count_))[:-1]
a.append(0)
a_count = [a[0]]
for (i, el) in enumerate(a[1:]):
    a_count.append(el - a[i])
for (i, el) in enumerate(oper):
    (l, r, d) = el
    d *= counter_[i]
    a_count[l - 1] += d
    a_count[r] -= d
a = list(accumulate(a_count))[:-1]
print(' '.join(map(str, a)))
