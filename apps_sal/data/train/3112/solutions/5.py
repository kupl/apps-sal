def avoid_obstacles(a):
    return min((n for n in range(1, max(a) + 2) if all((m % n for m in a))))
