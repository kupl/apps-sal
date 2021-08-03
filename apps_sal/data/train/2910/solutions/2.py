def small_enough(a, limit):
    if a[0] > limit:
        return False

    if len(a) > 1:
        return small_enough(a[1:], limit)

    return True
