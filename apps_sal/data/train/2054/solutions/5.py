import math

graph = []
colors = []


def dfs(u, p, color) -> bool:
    if color != colors[u]:
        return False
    for v in graph[u]:
        if v == p:
            continue
        if not dfs(v, u, color):
            return False
    return True


def check(u):
    for v in graph[u]:
        if not dfs(v, u, colors[v]):
            return False
    return True


def main():
    n = int(input())
    for _ in range(n):
        graph.append([])
    for i in range(n - 1):
        u, v = [int(x) - 1 for x in input().split()]
        graph[u].append(v)
        graph[v].append(u)
    nonlocal colors
    colors += list(map(int, input().split()))
    for u in range(n):
        for v in graph[u]:
            if colors[u] != colors[v]:
                if check(u):
                    print("YES")
                    print(u + 1)
                    return
                elif check(v):
                    print("YES")
                    print(v + 1)
                    return
                else:
                    print("NO")
                    return
    print("YES")
    print(1)


main()
