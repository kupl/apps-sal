from random import choice


def median(lst):
    return quickselect(lst, len(lst) // 2, len(lst) % 2 == 0)


def quickselect(lst, nth, even):
    # O(n) but what a pain to get right.
    pivot = choice(lst)
    smaller = [n for n in lst if n < pivot]
    n_equal = sum(n == pivot for n in lst)
    bigger = [n for n in lst if n > pivot]
    if even:
        if len(smaller) > nth:
            return quickselect(smaller, nth, True)
        elif len(smaller) == nth:
            return (pivot + quickselect(smaller, nth - 1, False)) / 2
        elif len(smaller) + n_equal > nth:
            return pivot
        elif len(smaller) + n_equal == nth:
            return (pivot + quickselect(bigger, nth - len(smaller) - n_equal, False)) / 2
        else:
            return quickselect(bigger, nth - len(smaller) - n_equal, True)
    else:
        if len(smaller) > nth:
            return quickselect(smaller, nth, False)
        elif len(smaller) + n_equal > nth:
            return pivot
        else:
            return quickselect(bigger, nth - len(smaller) - n_equal, False)
