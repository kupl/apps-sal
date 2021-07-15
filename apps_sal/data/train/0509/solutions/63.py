#!/usr/bin/env python3
# from typing import *
# %%
from collections import deque

# def solve(N: int, M: int, u: List[int], v: List[int], c: List[int]) -> List[str]:
def solve(start, adj):
    N = len(adj)
    ans = [0]*N
    ans[start] = 1
    que = deque([start])
    while que:
        frm = que.popleft()
        for to, c in adj[frm]:
            if ans[to]: continue
            if ans[frm] == c:
                ans[to] = c%N+1
            else:
                ans[to] = c
            que.append(to)
    return ans

# %%
# generated by online-judge-template-generator v4.7.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = list(map(int, input().split()))
    adj = {i:list() for i in range(N)}
    for i in range(M):
        u, v, c = list(map(int, input().split()))
        adj[u-1].append((v-1,c))
        adj[v-1].append((u-1,c))
    ans = solve(0, adj)
    for a in ans:
        print(a)


def __starting_point():
    main()

__starting_point()
