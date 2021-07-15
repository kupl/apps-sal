def super_size(n: int) -> int:
    """ Rearrange the integer into its largest possible value. """
    return int("".join(list(sorted(str(n), reverse=True))))
