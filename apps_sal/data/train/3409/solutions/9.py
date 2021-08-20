def fish(shoal):
    shoal_l = []
    for s in shoal:
        shoal_l.append(int(s))
        shoal_l.sort()
    max_size = 1
    food_count = 0
    amount_needed = 4
    for fishy in shoal_l:
        if max_size >= fishy:
            food_count += int(fishy)
        if food_count >= amount_needed:
            max_size += 1
            amount_needed += max_size * 4
    return max_size
