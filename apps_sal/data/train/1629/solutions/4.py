def exchange_sort(xs):
    xs7, xs9 = xs[:xs.count(7)], xs[len(xs) - xs.count(9):]
    return xs7.count(8) + xs9.count(8) + max(xs7.count(9), xs9.count(7))
