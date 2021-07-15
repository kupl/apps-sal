def split_all_even_numbers(numbers, way):
    split = (split_closest, split_furthest, split_max_equal, split_ones)[way]
    return sum(([n] if n % 2 else split(n) for n in numbers), [])


split_closest = lambda n: [n//2 + s * (n%4 == 0) for s in (-1, 1)]
split_furthest = lambda n: [1, n-1]
split_max_equal = lambda n: [n] if n % 2 else split_max_equal(n // 2) * 2
split_ones = lambda n: [1 for _ in range(n)]
