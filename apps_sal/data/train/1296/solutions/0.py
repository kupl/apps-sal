import sys
sys.setrecursionlimit(10 ** 8)
MOD = 10 ** 9 + 7
fac = [0] * (10 ** 5 + 1)


def pre():
    fac[0] = 1
    for i in range(1, 10 ** 5 + 1):
        fac[i] = fac[i - 1] * i
        fac[i] = fac[i] % MOD


def dfs(gp, vertex, visited, deg, ans):
    visited[vertex] = 1
    stack = []
    stack.append(vertex)
    while len(stack) > 0:
        vertex = stack.pop()
        ans = ans % MOD * fac[deg[vertex]] % MOD
        ans %= MOD
        for i in gp[vertex]:
            if not visited[i]:
                visited[i] = 1
                if vertex in gp[i]:
                    deg[i] -= 1
                stack.append(i)
    return ans % MOD


pre()
for __ in range(eval(input())):
    n = eval(input())
    deg = [0] * (n + 1)
    st = [[] for __ in range(n + 1)]
    for _ in range(n - 1):
        (a, b) = list(map(int, sys.stdin.readline().split()))
        st[a].append(b)
        st[b].append(a)
        deg[a] += 1
        deg[b] += 1
    k = eval(input())
    visited = [0] * (n + 1)
    print(dfs(st, k, visited, deg, 1) % MOD)
