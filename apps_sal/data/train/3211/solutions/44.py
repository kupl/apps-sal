def is_even(x):
    return x % 2 == 0


def divide(weight):
    if is_even(weight):
        if is_even(weight / 2):
            return True
        else:
            if is_even(weight / 2 + 1) and is_even(weight / 2 - 1) and (weight > 2):
                return True
            return False
    else:
        return False
