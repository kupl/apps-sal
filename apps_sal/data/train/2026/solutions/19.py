from sys import stdin
from math import inf


def main():
    (n, d) = readline()
    a = [0] + list(readline()) + [0]
    x = [0] * n
    y = [0] * n
    for i in range(n):
        (x[i], y[i]) = readline()
    return dijkstra(n, d, a, x, y)


def readline():
    return list(map(int, stdin.readline().strip().split()))


def dijkstra(n, d, a, x, y):
    lower_cost = [inf] * n
    lower_cost[0] = 0
    visited = [False] * n
    for i in range(n - 1):
        position = minimum(n, visited, lower_cost)
        visited[position] = True
        for k in range(n):
            if not visited[k]:
                diff = lower_cost[position] + d * (abs(x[k] - x[position]) + abs(y[k] - y[position])) - a[position]
                if lower_cost[k] > diff:
                    lower_cost[k] = diff
    return lower_cost[-1]


def minimum(n, visited, lower_cost):
    lower_value = inf
    position = 0
    for j in range(n):
        if visited[j] or lower_value <= lower_cost[j]:
            continue
        lower_value = lower_cost[j]
        position = j
    return position


def __starting_point():
    print(main())


__starting_point()
