from collections import deque
from operator import itemgetter


def group_cities(seq):
    seq_by_length = {}
    for s in seq:
        l = len(s)
        if l in seq_by_length:
            seq_by_length[l].append(s)
        else:
            seq_by_length[l] = [s]

    groups = []
    for elems in seq_by_length.values():
        to_check = deque(set(elems))

        while to_check:
            cur_check = to_check.pop()
            group, check = [cur_check], cur_check.lower() * 2

            for c in to_check.copy():
                if c.lower() in check:
                    group.append(c)
                    to_check.remove(c)

            groups.append(sorted(group))

    return sorted(sorted(groups, key=itemgetter(0)), key=len, reverse=True)
