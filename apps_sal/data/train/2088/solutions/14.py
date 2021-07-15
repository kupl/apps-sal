# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/9/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, A):
    dp = [[N for _ in range(N+1)] for _ in range(N)]
    for i in range(N):
        dp[i][0] = 0
        dp[i][1] = 1
    
    for l in range(2, N+1):
        for i in range(N-l+1):
            for j in range(1, l):
                dp[i][l] = min(dp[i][l], dp[i][j] + dp[i+j][l-j])
            
            # j = 0
            # while j < l // 2 and A[i+j] == A[i+l-j-1]:
            #     j += 1
            # if j >= l // 2:
            #     dp[i][l] = min(dp[i][l], 1)
            # elif j > 0:
            #     dp[i][l] = min(dp[i][l], 1 + dp[i+j][l-2*j])
            #     for k in range(i+j, i+l-j):
            #         dp[i][l] = min(dp[i][l], 1 + dp[i+j][k-i-j] + dp[k][l - 2 * j-1])
            
            if i + 1 < N and A[i] == A[i+l-1]:
                dp[i][l] = max(1, dp[i+1][l-2])
            else:
                dp[i][l] = min(dp[i][l], 1 + dp[i][l-1])
                if i + 1 < N:
                    dp[i][l] = min(dp[i][l], 1 + dp[i+1][l-1])
                    
            for j in range(i + 1, i + l - 2):
                if A[i] == A[j]:
                    dp[i][l] = min(dp[i][l], max(dp[i+1][j-i-1], 1) + max(dp[j+1][i+l-j-1], 1))
                if A[j] == A[i+l-1]:
                    dp[i][l] = min(dp[i][l], max(dp[i][j-i], 1) + max(dp[j+1][i + l - j - 2], 1))

    return dp[0][N]
    

N = int(input())
A = [int(x) for x in input().split()]
print(solve(N, A))
