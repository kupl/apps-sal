from collections import Counter


def modes(data):
    count = Counter(data)
    m = max(count.values()) if len(set(count.values())) > 1 else 0
    return sorted((item for (item, number) in count.items() if 0 < m == number))
