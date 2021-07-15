def close_compare(a: int, b: int, margin: int=0) -> int:
    """ Check if `a` is lower than, close to, or higher than `b`. """
    return 0 if (abs(a - b) <= margin if margin else a == b) else 1 if a > b else -1
