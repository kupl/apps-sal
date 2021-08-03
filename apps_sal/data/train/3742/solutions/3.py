from collections import Counter


def modes(data):
    c = Counter(data)
    m = max(c.values())
    if min(c.values()) == m:
        return []
    return [key for key in sorted(c) if c[key] == m]
