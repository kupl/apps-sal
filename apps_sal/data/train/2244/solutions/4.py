from heapq import heappop, heappush
import sys
input = sys.stdin.readline

"""
f(x) = （一番上の長方形の左端がxに来るときのコストの最小値） を関数ごと更新していきたい
更新後をg(x)とする
g(x) = |x-L| + min_{-width_1 \leq t\leq width_2} f(x+t), 前回の幅、今回の幅
常に、区間上で最小値を持ち傾きが1ずつ変わる凸な関数であることが維持される。（区間は1点かも）
傾きが変わる点の集合S_f = S_f_lower + S_f_upperを持っていく。
S_f_lower, S_upperは一斉に定数を足す：変化量のみ持つ
"""

N = int(input())
LR = [[int(x) for x in input().split()] for _ in range(N)]

L, R = LR[0]
S_lower = [-L]
S_upper = [L]
min_f = 0
add_lower = 0
add_upper = 0
prev_w = R - L


def push_L(x): return heappush(S_lower, -x)
def push_R(x): return heappush(S_upper, x)
def pop_L(): return -heappop(S_lower)
def pop_R(): return heappop(S_upper)


for L, R in LR[1:]:
    w = R - L
    add_lower -= w
    add_upper += prev_w
    x = pop_L() + add_lower
    y = pop_R() + add_upper
    a, b, c, d = sorted([x, y, L, L])
    push_L(a - add_lower)
    push_L(b - add_lower)
    push_R(c - add_upper)
    push_R(d - add_upper)
    min_f += c - b
    prev_w = w

print(min_f)
