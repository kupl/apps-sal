import sys
n = int(input())
for x in range(n):
    l, r = list(map(int, input().split()))
    a = 0
    while l <= r:
        a = l
        l += (~l) & (-~l)
    sys.stdout.write(str(a) + '\n')
