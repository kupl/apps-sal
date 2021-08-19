import enum


class IterDirection(enum.Enum):
    """ Direction in which we iterate/walk. """
    TowardsRight = (1,)
    TowardsLeft = 2


def unflatten(arr, depth):

    def is_iterable(obj):
        try:
            iter(obj)
        except TypeError:
            return False
        else:
            return True

    def walk(arr, direction):
        if direction == IterDirection.TowardsLeft:
            a = arr[::-1]
        else:
            a = list(arr)
        index = 0

        def walk_subarray(subarray):
            if direction == IterDirection.TowardsRight:
                yield list(walk(current_element, direction))
            else:
                yield list(walk(current_element, direction))[::-1]
        while index < len(a):
            current_element = a[index]
            if is_iterable(current_element):
                yield from walk_subarray(current_element)
                index += 1
            else:
                n_elements_left = len(arr[index:])
                remainder = current_element % n_elements_left
                if remainder < 3:
                    yield current_element
                    index += 1
                else:
                    if direction == IterDirection.TowardsLeft:
                        yield a[index:index + remainder][::-1]
                    else:
                        yield a[index:index + remainder]
                    index += remainder
    from itertools import cycle, islice
    directions = (IterDirection.TowardsRight, IterDirection.TowardsLeft)
    arr_copy = list(arr)
    for direction in islice(cycle(directions), depth):
        if direction == IterDirection.TowardsLeft:
            arr_copy = list(walk(arr_copy, IterDirection.TowardsLeft))[::-1]
        else:
            arr_copy = list(walk(arr_copy, IterDirection.TowardsRight))
    return arr_copy
