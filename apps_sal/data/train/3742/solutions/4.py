from collections import Counter


def modes(data):
    result = []
    counts = Counter(data)
    if len(set(counts.values())) > 1:
        result += sorted((k for (k, v) in list(counts.items()) if v == max(counts.values())))
    return result
