from itertools import chain


def split_all_even_numbers(lst, way):

    def convert(n):
        s = 1 - n // 2 % 2
        return [n] if n % 2 else [n // 2 - s, n // 2 + s] if way == 0 else [1, n - 1] if way == 1 else [1] * n if way == 3 else split_all_even_numbers([n // 2] * 2, 2)
    return list(chain(*map(convert, lst)))
