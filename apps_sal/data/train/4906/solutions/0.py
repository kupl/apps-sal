def traffic_lights(road, n):
    lightsIdx = [(i, 6 * (c != 'G')) for i, c in enumerate(road) if c in 'RG']
    car, ref = road.find('C'), road.replace('C', '.')
    mut, out = list(ref), [road]

    for turn in range(1, n + 1):

        for i, delta in lightsIdx:
            state = (delta + turn) % 11
            mut[i] = 'G' if state < 5 else 'O' if state == 5 else 'R'

        car += car + 1 >= len(road) or mut[car + 1] in '.G'

        if car < len(road):
            old, mut[car] = mut[car], 'C'
        out.append(''.join(mut))
        if car < len(road):
            mut[car] = old

    return out
