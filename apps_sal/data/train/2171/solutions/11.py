from collections import defaultdict, deque, Counter, OrderedDict
from bisect import insort, bisect_right, bisect_left
import threading


def main():
    n = int(input())
    adj = [[] for i in range(n + 1)]
    for i in range(n - 1):
        (a, b) = list(map(int, input().split()))
        (a, b) = (a - 1, b - 1)
        adj[a].append(b)
        adj[b].append(a)
    init = [int(i) for i in input().split()]
    goal = [int(i) for i in input().split()]
    visited = [0] * n
    par = [[] for i in range(n)]
    dq = deque()
    dq.append((0, 0))
    while len(dq) > 0:
        (s, p) = dq.pop()
        if visited[s]:
            continue
        visited[s] = 1
        par[p].append(s)
        for i in adj[s]:
            dq.append((i, s))
    par[0] = par[0][1:]
    ans = []
    dq = deque()
    dq.append((0, 0, 0, 0))
    while len(dq) > 0:
        (s, l, fo, fe) = dq.pop()
        if l % 2 == 0:
            if fe % 2 == 1:
                init[s] = 1 - init[s]
        elif fo % 2 == 1:
            init[s] = 1 - init[s]
        if init[s] != goal[s]:
            ans.append(s + 1)
            if l % 2:
                fo += 1
            else:
                fe += 1
        for j in par[s]:
            dq.append((j, l + 1, fo, fe))
    print(len(ans))
    print('\n'.join(map(str, ans)))


def __starting_point():
    """sys.setrecursionlimit(200000)
    threading.stack_size(10240000)"""
    thread = threading.Thread(target=main)
    thread.start()


__starting_point()
