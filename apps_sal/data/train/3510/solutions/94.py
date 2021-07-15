def count_red_beads(n):
    beads = 0
    if n < 2:
        return 0
    else: 
        for i in range(n-1):
            beads += 2 
    return beads 
