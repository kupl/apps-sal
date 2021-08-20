import sys
(n, m, c) = list(map(int, input().split()))
li = []
max = 0
for i in range(1, 51):
    print(1, 1, n, 1, m, i, i)
    sys.stdout.flush()
    ans = int(input())
    if ans > max:
        max = ans
        deal = i
print(3)
for i in range(n):
    print(' '.join([str(deal)] * m))
