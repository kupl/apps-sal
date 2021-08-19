def shorten_to_date(x):
    xs = x.rsplit(', ', 1)
    print(xs)
    xs.pop(1)
    print(xs)
    short_date = ' '
    return short_date.join(xs)
