def count_red_beads(n):
    beads = ''
    for i in range(n - 1):
        beads += 'B'
        beads += 'RR'
    beads += 'B'
    return beads.count('R')
