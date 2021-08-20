def sort_transform(arr):

    def d(x):
        return ''.join(map(chr, [x[0], x[1], x[-2], x[-1]]))
    b = d(sorted(arr))
    return '-'.join((d(arr), b, d(sorted(arr, reverse=True)), b))
