def spinning_rings(inner_max, outer_max):
    inner, outer = 0, 0
    while True:
        inner -= 1
        outer += 1

        if inner % (inner_max + 1) == outer % (outer_max + 1):
            return outer
