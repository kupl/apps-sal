def count_red_beads(n):
    if n < 2:
        return 0
    else:
        count = 2
        for i in range(2, n):
            count += 2

        return count
