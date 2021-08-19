def unusual_sort(array):

    def _isdigit(d):
        return type(d) == int or (type(d) == str and d.isdigit())
    digits = [d for d in array if _isdigit(d)]
    nondigits = [n for n in array if not _isdigit(n)]
    digits.sort(key=lambda d: int(d) if type(d) == str else d - 0.1)
    nondigits.sort()
    return nondigits + digits
