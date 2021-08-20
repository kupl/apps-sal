from itertools import permutations


def is_perfect(square):
    return round(square ** 0.5) ** 2 == square


def permuted(n):
    return (int(''.join(p)) for p in set(permutations(str(n))))


def perfect_permutations(n):
    return tuple((p for p in permuted(n) if is_perfect(p)))


def next_perfectsq_perm(lower_limit, k):
    root = int(lower_limit ** 0.5) + 1
    while True:
        square = root ** 2
        if not '0' in str(square):
            p = perfect_permutations(square)
            if len(p) == k:
                return max(p)
        root += 1
