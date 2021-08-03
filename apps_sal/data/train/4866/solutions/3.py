def split_all_even_numbers(numbers, way):
    split = (split_closest, split_furthest, split_max_equal, split_ones)[way]
    return sum(([n] if n % 2 else split(n) for n in numbers), [])


def split_closest(n): return [n // 2 + s * (n % 4 == 0) for s in (-1, 1)]
def split_furthest(n): return [1, n - 1]
def split_max_equal(n): return [n] if n % 2 else split_max_equal(n // 2) * 2
def split_ones(n): return [1 for _ in range(n)]
