n = int(input())
INF = 10**9
csum = 0
min_b = INF
for _ in range(n):
    a,b = list(map(int, input().split()))
    csum += a
    if a > b:
        min_b = min(min_b,b)

if min_b == INF:
    print((0))
else:
    ans = csum-min_b
    print(ans)


# a_down_sum = 0
# top_diff = 0
# for _ in range(n):
#     a,b = map(int, input().split())
#     if a < b:
#         a_down_sum += a
#     else:
#         top_diff = max(top_diff,a-b)


