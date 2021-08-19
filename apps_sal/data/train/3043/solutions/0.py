def print_nums(*arr):
    if not arr:
        return ''
    ln = len(str(max(arr)))
    return '\n'.join((str(c).zfill(ln) for c in arr))
