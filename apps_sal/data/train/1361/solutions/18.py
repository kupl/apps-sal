from itertools import accumulate
(n1, k1) = map(int, input().split())
last = list(map(int, input().split()))
temp = 10 ** 9 + 7
for i in range(k1):
    last = list(accumulate(last))
for i in last:
    print(i % temp, end=' ')
