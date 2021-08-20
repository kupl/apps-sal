def as_str(xs):
    return ''.join(map(chr, xs[:2] + xs[-2:]))


def sort_transform(arr):
    return '-'.join([as_str(arr), as_str(sorted(arr)), as_str(sorted(arr, reverse=True)), as_str(sorted(arr))])
