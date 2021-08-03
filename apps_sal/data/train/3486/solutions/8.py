from collections import deque


def find_last(n, m):
    circle = deque(range(1, n + 1))
    coin = 0
    for _ in range(1, n):
        coin += m if len(circle) <= m else (2 * len(circle)) - m
        circle.rotate(-(m - 1))
        circle.popleft()
    return (circle[0], coin)
