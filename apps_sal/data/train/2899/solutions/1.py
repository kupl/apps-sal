def bin_str(input):
    flips_needed = 0
    last_seen = '0'
    for c in input:
        if last_seen != c:
            flips_needed += 1
            last_seen = c
    return flips_needed
