from collections import Counter


def product(s: str) -> int:
    c = Counter(s)
    return c.get('!', 0) * c.get('?', 0)

