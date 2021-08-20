maxx = 2 * 10 ** 4 + 1
has = [1] * maxx
mod = 100000007
for i in range(2, maxx):
    for j in range(i, maxx, i):
        has[j] += 1
odd = 0
even = 0
th = 0
l = []
for i in has:
    if i == 3:
        th += 1
    elif i % 2 == 0:
        even += 1
    else:
        odd += 1
    l.append([th, even, odd])
for t in range(1, int(input()) + 1):
    (n, k1, k2) = list(map(int, input().split()))
    (p1, p2, p3, p4) = list(map(int, input().split()))
    th = l[k2][0] - l[k1 - 1][0]
    even = l[k2][1] - l[k1 - 1][1]
    odd = l[k2][2] - l[k1 - 1][2]
    summ = th * p1 % mod + odd * p2 % mod + even * p3 % mod
    print(summ)
