from collections import Counter
def find_dups_miss(arr):
    counter = Counter(arr)
    return [(max(counter) - min(counter) + 1) * (min(counter) + max(counter))//2 - sum(counter), [y for y in sorted(counter) if counter[y] > 1]]
