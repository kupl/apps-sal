from bisect import bisect, bisect_left
import sys
sys.setrecursionlimit(1000000)


def longest_subsequence(sequence):
    subsequence = [float("inf") for _ in range(len(sequence) + 1)]
    subsequence[0] = float("-inf")
    for value in sequence:
        j = bisect(subsequence, value)
        if subsequence[j - 1] != value:
            subsequence[j] = value
    return bisect_left(dp, float("inf")) - 1


def dfs(vertex):
    visited[vertex] = True
    value = a[vertex]
    j = bisect(subsequence, value)
    previous = subsequence[j]
    if subsequence[j - 1] != value:
        subsequence[j] = value
    ans[vertex] = bisect_left(subsequence, float("inf")) - 1
    for node in adjacent[vertex]:
        if not visited[node]:
            dfs(node)
    subsequence[j] = previous
    return


n = int(input())
a = list(map(int, input().split()))
adjacent = {i: [] for i in range(n)}
for _ in range(n - 1):
    node1, node2 = map(int, input().split())
    node1 -= 1
    node2 -= 1
    adjacent[node1].append(node2)
    adjacent[node2].append(node1)
visited = [False] * n
ans = [0] * n
subsequence = [float("inf") for _ in range(n + 1)]
subsequence[0] = float("-inf")
dfs(0)
[print(value) for value in ans]
