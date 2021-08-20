from itertools import islice
import operator


def is_sorted_and_how(arr):
    return 'yes, ascending' if is_sorted_with(arr, operator.le) else 'yes, descending' if is_sorted_with(arr, operator.ge) else 'no'


def is_sorted_with(arr, pred):
    return all((pred(x, y) for (x, y) in zip(arr, islice(arr, 1, None))))
