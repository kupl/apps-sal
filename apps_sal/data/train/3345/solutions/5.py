def find_uniq(arr):
    counts = {}
    result = {}
    for s in arr:
        hash = frozenset(s.strip().lower())
        counts[hash] = counts.get(hash, 0) + 1
        result[hash] = s
        if len(counts) > 1 and counts[max(counts, key=counts.get)] > 1:
            return result[min(counts, key=counts.get)]
