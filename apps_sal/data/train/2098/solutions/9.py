
"""

created by shuangquan.huang at 1/29/19

Let's iterate over final number of votes for The United Party of Berland.
We can see that all opponents should get less votes than our party,
and our party should get at least our chosen number of votes.

We can sort all voters by their costs, and solve the problem in two passes.
First, if we need to get 𝑥 votes, we should definitely buy all cheap votes for parties that have at least 𝑥 votes.
Second, if we don't have 𝑥 votes yet, we should by the cheapest votes to get 𝑥 votes.
We can see that this solution is optimal: consider the optimal answer, and see how many votes The United Party got.
We tried such number of votes, and we tried to achieve this number of votes by cheapest way, so we couldn't miss the
optimal answer. This can be implemented in 𝑂(𝑛2log𝑛) or even 𝑂(𝑛log𝑛).



"""

import collections
import time
import os
import sys
import bisect
import heapq


def solve(N, M, A):
    votes = [[] for _ in range(M + 1)]
    for p, v in A:
        votes[p].append(v)

    for p in range(1, M + 1):
        votes[p].sort()

    own = len(votes[1])
    votes = votes[2:]
    votes.sort(reverse=True, key=len)
    size = [len(v) for v in votes]
    if not size or own > size[0]:
        return 0

    nvotes = len(votes)
    ans = float('inf')
    for buy in range((size[0] - own) // 2 + 1, min(N, (N + 1) // 2 + 1) + 1):
        cost = 0
        target = own + buy
        done = 0

        for p in range(nvotes):
            if size[p] >= target:
                t = size[p] - target + 1
                cost += sum(votes[p][: t] or [0])
                done += t
            else:
                break
        if done >= buy:
            ans = min(ans, cost)
        else:
            more = buy - done
            q = []
            for p in range(nvotes):
                t = max(size[p] - target + 1, 0)
                q.extend(votes[p][t: t + more])
            q.sort()
            cost += sum(q[:more])
            ans = min(ans, cost)

    return ans


N, M = list(map(int, input().split()))
A = []
for i in range(N):
    p, v = list(map(int, input().split()))
    A.append((p, v))

print(solve(N, M, A))
