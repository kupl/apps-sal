from collections import Counter


def scramble(s1, s2):
    if not set(s2).issubset(set(s1)):
        return False
    s1_counts = Counter(s1)
    s2_counts = Counter(s2)
    s1_counts.subtract(s2_counts)
    return not any([x for x in list(s1_counts.items()) if x[1] < 0])
