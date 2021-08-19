from itertools import chain


def hyperrectangularity_properties(arr):
    (hr, arr) = ([], [arr])
    while 1:
        check = sum((isinstance(v, int) for v in arr))
        if check or not arr:
            if check == len(arr):
                return tuple(hr)
            break
        l = set(map(len, arr))
        if len(l) > 1:
            break
        hr.append(l.pop())
        arr = list(chain.from_iterable(arr))
