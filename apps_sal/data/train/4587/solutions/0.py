def range_parser(string):
    res = []
    for range_ in string.split(','):
        (first_last, _, step) = range_.partition(':')
        (first, _, last) = first_last.partition('-')
        res += range(int(first), int(last or first) + 1, int(step or 1))
    return res
