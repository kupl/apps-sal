def stringy(size: int) -> str:
    """ Take a size and return a string of alternating `1s` and `0s`. """
    return "".join([str(_ % 2) for _ in range(1, size + 1)])
