import re


def find_nth_occurrence(sb, s, n=1):
    r = list(re.finditer('(?=' + sb + ')', s))
    return r[n - 1].span()[0] if n <= len(r) else -1
