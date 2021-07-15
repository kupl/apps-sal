def spinning_rings(inner_max, outer_max):
    inner = inner_max
    outer = 1
    moves = 1
    while inner != outer:
        if outer > inner_max:
            jump = outer_max + 1 - outer
        elif inner > outer_max:
            jump = inner - outer_max
        elif inner > outer:
            jump = (inner - outer + 1) // 2
        elif inner == (outer_max + 1 - outer):
            jump = inner
        else:
            jump = min(inner + 1, outer_max + 1 - outer)
        outer = (outer + jump) % (outer_max + 1)
        inner = (inner - jump) % (inner_max + 1)
        moves += jump
    return moves
