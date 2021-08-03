def advice(agents, n):
    frontier = {(x, y) for x, y in agents if 0 <= x < n and 0 <= y < n}
    bag = {(x, y) for x in range(n) for y in range(n)}
    if frontier == bag:
        return []
    while frontier and bag > frontier:
        bag -= frontier
        frontier = {pos for x, y in frontier for pos in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)) if pos in bag}
    return sorted(bag)
