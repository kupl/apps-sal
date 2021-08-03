from itertools import groupby


def count_adjacent_pairs(st):
    return len([name for name, group in groupby(st.lower().split(' ')) if len(list(group)) >= 2])
