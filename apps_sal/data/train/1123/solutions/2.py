from collections import defaultdict
import sys
sys.setrecursionlimit(10000)


def dfs(n):
    ans = set()
    queue = [n]
    bool[n] = True
    ans.add(n)
    while queue != []:
        z = queue.pop(0)
        ans.add(z)
        for j in hash[z]:
            if bool[j] == False:
                bool[j] = True
                queue.append(j)
    return ans


t = int(input())
for _ in range(t):
    ans = []
    hash = defaultdict(list)
    (n, m) = map(int, sys.stdin.readline().strip().split())
    for i in range(m):
        (a, b) = map(int, sys.stdin.readline().strip().split())
        hash[a].append(b)
        hash[b].append(a)
    for i in range(n):
        bool = [False] * n
        z = dfs(i)
        hash[i] = z
    q = int(input())
    for i in range(q):
        (a, b) = map(int, sys.stdin.readline().strip().split())
        dfs(a)
        if b in hash[a]:
            z = 'YO'
            sys.stdout.write(z)
            print()
        else:
            z = 'NO'
            sys.stdout.write(z)
            print()
