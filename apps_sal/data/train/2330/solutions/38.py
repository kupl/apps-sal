def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

"""
頂点がN個、辺がN - 1本あります
1110
任意の辺を一つ取り除くとサイズ1の連結成分が作れる
任意の辺を一つ取り除くとサイズ2の連結成分が作れる
任意の辺を一つ取り除くとサイズ3の連結成分が作れる

どの辺を一つ取り除いてもサイズ4の連結成分は作れない

サイズ1の連結成分が作れること、サイズnの連結成分は作れないことは自明
サイズiの連結成分が作れるなら、サイズn - iの連結成分が作れる
単純な木構造から考えよう
・パスグラフ
・スターグラフ

・パスグラフ
1(1がN - 1個) + 0になる
・スターグラフ
10...010になる

他のものは作れないか
連結成分iのものが作れる条件、作れない条件
作れない条件が知りたい　単体であれば必ず作れる
（連結成分iが作れ、jが作れない）が成り立たない場合がある？
部分木から考えていく
大きさ2のパスグラフは11
これをrootにつけると 110になる
大きさ3のスターグラフは101
これをrootにつけると1010になる

大きさnのグラフにパス状に/スター状に繋げていくと
1 - 2のグラフに
パス状に3を繋げると 110
スター状に繋げると 110 ここまでは同じ
1 - 2 - 3のグラフに
パス状に繋げると 1110
スター状に繋げると 1010

パスグラフに辺を加えて連結成分jが作れないようにしよう

11010110は作れるか
一方をパスグラフに、一方をスターグラフにする?
1 - 2の状態でスタート
もしS[i] = 1なら親要素にi + 2をつけ、それを親要素にする
もしS[i] = 0なら現在の親要素につける
"""

S = input()
N = len(S)
# この条件を満たしていると木を作ることができる
if S[N - 1] == "1" or S[N - 2] == "0" or S[0] == "0":
    print(-1)
else:
    for i in range(N - 1):
        if S[i] != S[N - i - 2]:
            print(-1)
            return
    ans = []
    parent = 1 # 現在のparent
    for i in range(N - 1):
        if S[i] == "1":
            # パスグラフ状
            ans.append([parent, i + 2])
            parent = i + 2 # parent変更
        else:
            # スターグラフ状
            ans.append([parent, i + 2])
    for i in ans:
        print(i[0], i[1])
