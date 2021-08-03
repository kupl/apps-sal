def shortest_time(speed):
    import itertools
    from collections import Counter
    times = []
    for elem in itertools.combinations(speed, 2):
        end1 = [x for x in elem]
        base1 = list((Counter(speed) - Counter(end1)).elements())
        for i in itertools.combinations(end1, 1):
            base2 = [x for x in base1 + [i[0]]]
            if sum(end1) != 2 * end1[0]:
                end2 = [x for x in end1 if x != i[0]]
            else:
                end2 = [end1[0]]
            for j in itertools.combinations(base2, 2):
                end3 = [x for x in end2 + [j[0], j[1]]]
                base3 = list((Counter(base2) - Counter(j)).elements())
                for k in itertools.combinations(end3, 1):
                    base4 = [x for x in base3 + [k[0]]]
                    times += [max(elem) + i[0] + max(j) + k[0] + max(base4)]
    return min(times)
