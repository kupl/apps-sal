MODULUS = 12345787


def circular_limited_sums(max_n, max_fn):
    total = 0
    for initial in range(max_fn + 1):
        counts = {v: 0 for v in range(max_fn + 1)}
        counts[initial] = 1
        for n in range(1, max_n):
            new_counts = {}
            for v in range(max_fn + 1):
                new_counts[v] = sum(counts[v_prev] for v_prev in range(max_fn - v + 1)) % MODULUS
            counts = new_counts
        total += sum(counts[v] for v in range(max_fn - initial + 1)) % MODULUS
    return total % MODULUS
