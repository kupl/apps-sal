def split0(x):
    return [x] if x & 1 else [(x >> 1) - ((x & 2) >> 1 ^ 1), (x >> 1) + ((x & 2) >> 1 ^ 1)]


def split1(x):
    return [x] if x & 1 else [1, x - 1]


def split2(x):
    return [x] if x & 1 else split2(x >> 1) * 2


def split3(x):
    return [x] if x & 1 else [1] * x


splits = (split0, split1, split2, split3)


def split_all_even_numbers(numbers, way):
    return [y for x in numbers for y in splits[way](x)]
