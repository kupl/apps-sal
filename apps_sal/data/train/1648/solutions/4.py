def spinning_rings(inner_max, outer_max):
    if inner_max == outer_max:
        if inner_max % 2:
            return (inner_max + 1) / 2
        return inner_max + 1
    if inner_max % 2:
        res = (inner_max + 1) / 2 if outer_max > (inner_max + 1) / 2 else (inner_max + 1 + (outer_max + 1) * ((inner_max + 1) // (outer_max + 1) - 1 + (((inner_max + 1) // (outer_max + 1) + 1) * (outer_max + 1)) % 2)) / 2
        return res
    if outer_max < inner_max:
        if outer_max % 2:
            a = 2 * (inner_max + 1) - (inner_max + 1) % (outer_max + 1)
            return a if (inner_max + 1) % (outer_max + 1) > (outer_max + 1) / 2 else a - (outer_max + 1) / 2
        else:
            a = inner_max + 1 - (inner_max - outer_max) % (outer_max + 1)
            b = (inner_max + 1 - a) // 2
            c = (outer_max + 1 + a) % 2
            return inner_max - b + 1 if not c else (inner_max - outer_max + a) / 2
    if outer_max > inner_max:
        k = (outer_max + 1) // (inner_max + 1)
        a = (k + 1) * (inner_max + 1) + ((outer_max + 1) % (inner_max + 1)) / 2
        return a if not ((outer_max + 1) % (inner_max + 1)) % 2 else 2 * (outer_max + 1) - (outer_max - inner_max / 2) - ((outer_max + 1) % (inner_max + 1) + 1) / 2
