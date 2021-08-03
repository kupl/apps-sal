from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
words = [deque(input().rstrip()) for _ in range(N)]

# 深さLのfull treeの小さい方を計算してみる


def G_small():
    G = [0] * 100
    G_cum = [0] * 100
    G[0] = 1
    G_cum[0] = 1
    for n in range(1, 100):
        can_make = set(G_cum[n - 1] ^ G_cum[x] for x in range(n)) | set([G_cum[n - 1]])
        rest = set(range(n + 10)) - can_make
        G[n] = min(rest)
        G_cum[n] = G_cum[n - 1] ^ G[n]
    return G

# print([(n,G[n]) for n in range(100)])
# G[n] = 2**ord_2(n+1)
# 値がわかれば証明は易しい


def G(n):
    n += 1
    x = 1
    while not n & 1:
        n >>= 1
        x <<= 1
    return x


def calc_grandy(words, L):
    if not words:
        return G(L)
    if len(words) == 1 and words[0] == deque():
        return 0
    words_0 = []
    words_1 = []
    for word in words:
        first = word.popleft()
        if first == '0':
            words_0.append(word)
        else:
            words_1.append(word)
    return calc_grandy(words_0, L - 1) ^ calc_grandy(words_1, L - 1)


g = calc_grandy(words, M)

answer = 'Alice' if g != 0 else 'Bob'
print(answer)
