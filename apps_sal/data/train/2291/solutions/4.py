# -*- coding: utf-8 -*-
""" outputの時間比較 """
from sys import stdin, stdout
import numpy as np
# import sys
# sys.setrecursionlimit(10**4)

def _li(): return list(map(int, stdin.readline().split()))
def _li_(): return list([int(x)-1 for x in stdin.readline().split()])
def _lf(): return list(map(float, stdin.readline().split()))
def _ls(): return stdin.readline().split()
def _i(): return int(stdin.readline())
def _f(): return float(stdin.readline())
def _s(): return stdin.readline()[:-1]
d_in = lambda: int(stdin.readline())  # N = d_in()
ds_in = lambda: list(map(int, stdin.readline().split()))  # List = ds_in()
def print_list(s):
    stdout.write(' '.join(list(map(str, s))) + '\n')
    # stdout.flush()
def print_single(s):
    stdout.write(str(s) + '\n')
    # stdout.flush()


# N = _i()
# D_list = np.array([_i() for _ in range(N)])
N = d_in()
D_list = np.array([d_in() for _ in range(N)])


idx = np.argsort(D_list)
sorted_D = D_list[idx]
mapping = []
for j in idx:
    mapping.append(j+1)

# 解説を参考に実装
# Dのスコアが大きい方から小さい方へ伸びる有向エッジとみなす
# valueはノードから出ている有向エッジを切った場合の部分木の大きさ
nodes = [1] * N
ans = []
cost = [[0, 1] for _ in range(N)]
# 葉っぱから見て，[エッジにたどり着くまでのコスト, 自分も含めた子ノードの数]
for i in range(N-1, 0, -1):
    d = sorted_D[i]
    sub = nodes[i]
    target = d + 2*sub - N
    cand = np.searchsorted(sorted_D[:i], target)
    if (sorted_D[cand] != target) or (cand == i):
        print((-1))
        return
    else:
        ans.append((mapping[i], mapping[cand]))
        nodes[cand] += nodes[i]
        cost[cand][0] += (cost[i][0] + cost[i][1])
        cost[cand][1] += cost[i][1]

# 1番目のノードについてチェック
if cost[0][0] != sorted_D[0]:
    print((-1))
    return
else:
    for a in ans:
        # print(a[0], a[1])
        print_list(a)

