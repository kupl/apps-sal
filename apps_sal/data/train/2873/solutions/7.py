def josephus_survivor(n, k):
    circle = list(range(1, n + 1))
    i = 0
    while len(circle) > 1:
        i = (i - 1 + k) % len(circle)
        circle.pop(i)
    return circle[0]
