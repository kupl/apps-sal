from itertools import chain


def split_all_even_numbers(lst, way):

    def convert(n):
        s = 1 - (n // 2) % 2                               # Shift for closest odd numbers
        return ([n] if n % 2 else             # Is already odd
                [n // 2 - s, n // 2 + s] if way == 0 else        # Two closest odd sum
                [1, n - 1] if way == 1 else        # Two farthest odd sum
                [1] * n if way == 3 else        # Split in ones
                split_all_even_numbers([n // 2] * 2, 2))     # Split in highest possible odds

    return list(chain(*map(convert, lst)))
