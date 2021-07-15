from collections import defaultdict

def solve(strings):
    indices_by_chars = defaultdict(list)
    for i, s in enumerate(strings):
        indices_by_chars[frozenset(s)].append(i)
    return sorted(sum(js) for js in list(indices_by_chars.values()) if len(js) > 1)

