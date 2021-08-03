def merge(line):
    mrg, lst, l, fr = [], [x for x in line if x], len(line), 0
    for e in lst:
        if not fr:
            fr = e
        elif fr == e:
            mrg.append(fr + e)
            fr = 0
        else:
            mrg.append(fr)
            fr = e

    mrg.append(fr)
    while len(mrg) < l:
        mrg.append(0)
    return mrg
