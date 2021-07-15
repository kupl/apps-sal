# cook your dish here
import bisect
# def recur(s_i, e_i, end_i):
#     # if end_i in dp[s_i] and e_i in dp[s_i][end_i]:
#     #     return dp[s_i][end_i][e_i]
        
#     inside = 0
#     for i in range(s_i+1, e_i):
#         if b_l[i] < k:
#             if e_i not in dp[i]:
#                 dp[i][e_i] = 0
#                 bi_i = bisect.bisect_left(b_inv[b_l[i]+k], i)
#                 for ind in b_inv[b_l[i]+k][bi_i:]:
#                     if i < ind < e_i:
#                         dp[i][e_i] = max(dp[i][e_i], recur(i, ind, e_i))
#             inside = max(inside, dp[i][e_i])
#     outside = 0
#     for i in range(e_i+1, min(n, end_i)):
#         if b_l[i] < k:
#             if end_i not in dp[i]:
#                 dp[i][end_i] = 0
#                 bi_i = bisect.bisect_left(b_inv[b_l[i]+k], i)
#                 for ind in b_inv[b_l[i]+k][bi_i:]:
#                     if i < ind < end_i:
#                         dp[i][end_i] = max(dp[i][end_i], recur(i, ind, end_i))
#             outside = max(outside, dp[i][end_i])
                    
#     # if end_i not in dp[s_i]:
#     #     dp[s_i][end_i] = {}
#     # dp[s_i][end_i].update({e_i: v_l[s_i] + v_l[e_i] + outside + inside})
#     # return dp[s_i][end_i][e_i]
#     return v_l[s_i] + v_l[e_i] + outside + inside
    
n, k1, *l = map(int, input().split())
v_l, b_l = l[:n], l[n:]

b_inv = {key:[] for key in range(2*k1)}
for i in range(n):
    b_l[i] -= 1
    b_inv[b_l[i]].append(i)

dp = [[0 for _ in range(n)] for _ in range(n)]
for k in range(1, n):
    for j in range(n-2, -1, -1):
        if j+k >= n:
            continue
        
        dp[j][j+k] = max(dp[j][j+k], dp[j][j+k-1])
        if b_l[j+k] >= k1:
            left = bisect.bisect_right(b_inv[b_l[j+k]-k1], j)
            
            if b_l[j+k] >= k1:
                for i in b_inv[b_l[j+k]-k1][left:]:
                    if i > j+k:
                        break
                    if i > j:
                        dp[j][j+k] = max(dp[j][j+k], dp[j][i-1]+dp[i][j+k])
                
        if b_l[j+k]-k1 == b_l[j]:
            if j+k-1 < n:
                dp[j][j+k] = max(dp[j][j+k], v_l[j+k]+v_l[j]+dp[j+1][j+k-1])
            else:
                dp[j][j+k] = max(dp[j][j+k], v_l[j+k]+v_l[j])
        
# dp = [{} for _ in range(n)]
# ans = 0
# for i in range(n):
#     if b_l[i] < k:
#         if n+1 not in dp[i]:
#             dp[i][n+1] = 0
#             bi_i = bisect.bisect_left(b_inv[b_l[i]+k], i)
#             for ind in b_inv[b_l[i]+k][bi_i:]:
#                 if i < ind:
#                     dp[i][n+1] = max(dp[i][n+1], recur(i, ind, n+1))
#         ans = max(ans, dp[i][n+1])
# print(dp)
print(dp[0][-1])
