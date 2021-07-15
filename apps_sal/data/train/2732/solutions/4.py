from collections import Counter


sort_group = lambda c: (c.isdecimal(), c.isupper(), c.islower(), c)


def blocks(stg):
    groups, count = [], Counter(stg)
    while count:
        groups.append("".join(sorted(list(count.keys()), key=sort_group)))
        count -= Counter(list(count.keys()))
    return "-".join(groups)

