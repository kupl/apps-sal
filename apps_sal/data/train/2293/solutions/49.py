# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n = int(readline())
*a, = list(map(int, readline().split()))

top2 = [[i, 0] for i in a]
for i in range(n):
    i = 1 << i
    for j in range(1 << n):
        if j & i:
            top2[j] = list(sorted(top2[j ^ i] + top2[j]))[2:]

# print(top2)

ans = list(map(sum, top2))

for i in range(1, 1 << n):
    ans[i] = max(ans[i], ans[i - 1])
    print((ans[i]))
