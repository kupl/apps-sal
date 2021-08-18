from sys import stdin, stdout
import collections

Q = int(input())
ans = [0] * Q
for q in range(Q):

    N, K = [int(x) for x in stdin.readline().split()]
    s = input()
    res = N + 1

    if N == 1 or K == 1:
        ans[q] = 0
        continue

    prefix = [0] * (N + 1)

    for k in range(3):
        if k == 0:
            RGB = 'RGB'
        if k == 1:
            RGB = 'GBR'
        if k == 2:
            RGB = 'BRG'

        ssum = 0
        for i in range(N):
            letter = RGB[i % 3]
            if s[i] != letter:
                ssum += 1
            prefix[i + 1] = ssum
            if i >= K - 1:
                res = min(res, prefix[i + 1] - prefix[i + 1 - K])

    ans[q] = res

print(*ans, sep='\n')
