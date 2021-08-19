# cook your dish here
N = int(input())
Ps = list(map(int, input().strip().split(" ")))
# print(Ps)

sum = [0 for i in range(N)]
if N > 0:
    sum[0] = Ps[0]
if N > 1:
    sum[1] = Ps[0] + Ps[1]
if N > 2:
    sum[2] = max(Ps[0] + Ps[2], max(sum[1], Ps[1] + Ps[2]))


for i in range(3, N):
    sum[i] = max(sum[i - 2] + Ps[i], max(sum[i - 1], sum[i - 3] + Ps[i - 1] + Ps[i]))


print(sum.pop())
"""
23
"""
