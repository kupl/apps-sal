def spinning_rings(inner_max, outer_max):
    innerList = [0] + [i for i in range(inner_max, 0, -1)]
    outerList = [0] + [i for i in range(1, outer_max + 1)]

    tries = 1
    while True:
        if innerList[tries % (inner_max + 1)] == outerList[tries % (outer_max + 1)]:
            return tries
            break
        tries += 1
