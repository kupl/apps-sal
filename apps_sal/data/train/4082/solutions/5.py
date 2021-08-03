from enum import IntEnum


class Classification(IntEnum):
    UNORDERED = 0
    INCREASING = 1
    NOT_DECREASING = 2
    DECREASING = 3
    NOT_INCREASING = 4
    CONSTANT = 5


def sequence_classifier(arr):
    unordered = True
    increasing = True
    not_decreasing = True
    decreasing = True
    not_increasing = True
    constant = True

    previous_val = None

    for val in arr:
        if previous_val is None:
            previous_val = val
            continue

        if increasing and val <= previous_val:
            increasing = False

        if not_decreasing and val < previous_val:
            not_decreasing = False

        if decreasing and val >= previous_val:
            decreasing = False

        if not_increasing and val > previous_val:
            not_increasing = False

        if constant and val != previous_val:
            constant = False

        if not unordered and not increasing and not not_decreasing and not decreasing and not not_increasing and not constant:
            return Classification.UNORDERED

        previous_val = val

    if constant:
        return Classification.CONSTANT
    elif increasing:
        return Classification.INCREASING
    elif not_decreasing:
        return Classification.NOT_DECREASING
    elif decreasing:
        return Classification.DECREASING
    elif not_increasing:
        return Classification.NOT_INCREASING
    else:
        return Classification.UNORDERED
