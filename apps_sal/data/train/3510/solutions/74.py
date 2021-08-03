def count_red_beads(n):
    count = 0
    if n < 2:
        return count
    for i in range(2, n + 1):
        count += 2
    return count
