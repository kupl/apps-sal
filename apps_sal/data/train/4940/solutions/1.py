def shut_the_gate(farm):
    (start, regions) = (0, [])
    for (i, c) in enumerate(farm):
        if c == '|':
            if start != i:
                free = start == 0 and farm[0] != '|'
                regions.append([start, i, free, farm[start:i], False])
            start = i
    if start < len(farm) - 1:
        regions.append([start, i, True, farm[start:i + 1], False])
    if regions and regions[0][2] and regions[-1][2]:
        regions[0][-1] = True
        regions[-1][-1] = True
    f = [c for c in farm]
    for (start, stop, free, s, linked) in regions:
        s2 = '' if not linked else regions[0 if start > 0 else -1][3]
        removals = set()
        if free:
            removals |= {'H', 'C', 'R'}
        if 'H' in s + s2:
            removals |= {'A', 'V'}
        if 'R' in s + s2:
            removals |= {'V'}
        f[start:stop + 1] = ['.' if c in removals else c for c in f[start:stop + 1]]
    return ''.join(f)
