def longest(s1, s2):
    insieme = set()
    for char in s1 + s2:
        insieme.add(char)
    return ''.join(sorted(insieme))
