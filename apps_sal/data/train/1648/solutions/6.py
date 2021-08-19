def spinning_rings(inner_max, outer_max):
    i = inner_max
    o = 1
    moves = 1
    while i != o:
        if o > inner_max:
            jump = outer_max + 1 - o
        elif i > outer_max:
            jump = i - outer_max
        elif i > o:
            jump = (i - o + 1) // 2
        elif i == outer_max + 1 - o:
            jump = i
        else:
            jump = min(i + 1, outer_max + 1 - o)
        o = (o + jump) % (outer_max + 1)
        i = (i - jump) % (inner_max + 1)
        moves += jump
    return moves
