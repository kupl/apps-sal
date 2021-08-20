from collections import deque, defaultdict
import sys
stdin = sys.stdin
sys.setrecursionlimit(10 ** 7)


def li():
    return list(map(int, stdin.readline().split()))


def li_():
    return [int(x) - 1 for x in stdin.readline().split()]


def lf():
    return list(map(float, stdin.readline().split()))


def ls():
    return stdin.readline().split()


def ns():
    return stdin.readline().rstrip()


def lc():
    return list(ns())


def ni():
    return int(stdin.readline())


def nf():
    return float(stdin.readline())


(n, m) = li()
mod = 10 ** 7
table = defaultdict(set)
visit = defaultdict(int)
for i in range(m):
    (a, b, c) = li()
    table[a].add(a + c * mod)
    table[b].add(b + c * mod)
    table[a + c * mod].add(a)
    table[b + c * mod].add(b)
    table[a + c * mod].add(b + c * mod)
    table[b + c * mod].add(a + c * mod)
    visit[a] = 0
    visit[b] = 0
    visit[b + c * mod] = 0
    visit[a + c * mod] = 0
que = deque()
que.append((1, 0))
visit[1] = 1
ans = mod
while que:
    (x, cost) = que.popleft()
    visit[x] = 1
    if x == n:
        ans = min(ans, cost)
        break
    for y in table[x]:
        if visit[y] == 1:
            continue
        if x <= 10 ** 5 and mod <= y:
            que.append((y, cost + 1))
        else:
            que.appendleft((y, cost))
print(-1 if ans == mod else ans)
