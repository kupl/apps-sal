from sys import stdin
from math import inf


def readline():
    return list(map(int, stdin.readline().strip().split()))


def main():
    n, d = readline()
    a = [0] + list(readline()) + [0]
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = readline()
    lower_cost = [inf] * n
    lower_cost[0] = 0
    visited = [False] * n
    for i in range(n - 1):
        lower_value = inf
        position = 0
        for j in range(n):
            if not visited[j] and lower_value > lower_cost[j]:
                lower_value = lower_cost[j]
                position = j
        visited[position] = True
        for k in range(n):
            if not visited[k]:
                diff = lower_cost[position] + d * (abs(x[k] - x[position]) + abs(y[k] - y[position])) - a[position]
                if lower_cost[k] > diff:
                    lower_cost[k] = diff
    return lower_cost[-1]


def __starting_point():
    print(main())


__starting_point()
