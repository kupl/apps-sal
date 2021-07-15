def part_const(n, size, forbidden):

    ways, k, partitions = [0, n] + [0] * (n - 1), 1, 0
    while k:
        x, y, k = ways[k-1] + 1, ways[k] - 1, k -1
        while x <= y:
            ways[k] = x
            y, k = y - x, k + 1
        ways[k] = x + y
        if len(ways[:k + 1]) == size and forbidden not in ways[:k + 1]: partitions +=  1
    return partitions
