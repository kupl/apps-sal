from collections import deque
from sys import stdin
import psyco
psyco.full()

graph = [[]]
WHITE, GRAY, BLACK = 0, 1, 2


def notoriety(x, f_count):
    queue = deque([x])
    d = [0 for i in range(f_count + 1)]
    p = [0 for i in range(f_count + 1)]
    color = [WHITE for i in range(f_count + 1)]
    while len(queue) > 0:
        top = queue.pop()
        for node in graph[top]:
            if color[node] == WHITE:
                queue.appendleft(node)
                color[node], p[node], d[node] = GRAY, top, d[top] + 1
        color[top] = BLACK
    return sum(d) / (f_count * 1.0)


def main():
    groups = int(stdin.readline())
    for g in range(groups):
        global graph
        graph = [[]]
        no_of_friends = int(stdin.readline())
        for i in range(no_of_friends):
            graph.append(list(map(int, stdin.readline().split())))
        min_notoriety, popular = 10000000, -1
        for f in range(1, no_of_friends + 1):
            curr_not = notoriety(f, no_of_friends)
            if curr_not < min_notoriety:
                min_notoriety, popular = curr_not, f
        assert popular != -1
        print(popular, "%.6f" % min_notoriety)


def __starting_point():
    main()


__starting_point()
