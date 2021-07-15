def spinning_rings(inner_max, outer_max):
    i = 1
    while True:
        inner = -i % (inner_max + 1)
        outer = i % (outer_max + 1)
        if inner == outer:
            return int(i)
        elif inner < outer:
            i += inner + 1 if inner_max > outer_max else outer_max - outer + 1
        else:
            if inner > outer_max:
                i += inner - outer_max
            else:
                mid = (inner + outer) / 2
                if mid % 1 == 0:
                    i += mid - outer
                else:
                    i += min(inner, outer_max - outer) + 1
