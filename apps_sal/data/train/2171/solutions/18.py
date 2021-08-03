'''input
10
2 1
3 1
4 2
5 1
6 2
7 5
8 6
9 8
10 5
1 0 1 1 0 1 0 1 0 1
1 0 1 0 0 1 1 1 0 1
'''

from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(1500000)


def counter(num):
    if num == 0:
        return 1
    else:
        return 0


def flip_me(original, count, index):
    if count % 2 == 0:
        return original[index]
    else:
        return counter(original[index])


def dfs(graph, visited, ans, original, goal, change, node, dfs_stack):
    dfs_stack.append(node)
    while len(dfs_stack) > 0:
        node = dfs_stack.pop()
        visited[node] = True

        value = flip_me(original, change[node], node - 1)
        add = 0
        if goal[node - 1] == value:
            pass
        else:
            add = 1
            ans[node] = True

        flag = 0
        for i in graph[node]:
            if visited[i] == False:
                flag = 1
                for j in graph[i]:
                    if visited[j] == False:
                        change[j] += change[node] + add

                dfs_stack.append(node)
                dfs_stack.append(i)
                break

        if flag == 0:
            pass


def calculate(graph, original, goal, n):
    visited = dict()
    change = dict()
    for i in range(1, n + 1):
        visited[i] = False
        change[i] = 0
    ans = dict()
    dfs_stack = []
    dfs(graph, visited, ans, original, goal, change, 1, dfs_stack)
    return ans


# main starts
n = int(stdin.readline().strip())
graph = defaultdict(list)
for i in range(1, n + 1):
    graph[i]

for _ in range(n - 1):
    u, v = list(map(int, stdin.readline().split()))
    graph[u].append(v)
    graph[v].append(u)

original = list(map(int, stdin.readline().split()))
goal = list(map(int, stdin.readline().split()))
count = [0]
ans = calculate(graph, original, goal, n)
print(len(ans))
for i in ans:
    print(i)
