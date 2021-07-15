from collections import Counter

def exchange_sort(sequence):
    """Greedy algorithm based on permutation cycle decomposition:
    1. Search for transposition placing TWO elements correctly.
    2. Search iteratively for transposition placing ONE elements correctly."""
    swaps, cnt = 0, Counter()
    for a, b in zip(sequence, sorted(sequence)):
        if cnt[b,a] > 0:
            cnt[b,a] -= 1
            swaps += 1
        elif a != b:
            cnt[a,b] += 1
    # Special case: as there are only three keys at most,
    # all remaining cycles will be 3-length cycles that
    # need 2 transpositions to place 3 elements correctly.
    return swaps + sum(cnt.values()) // 3 * 2
