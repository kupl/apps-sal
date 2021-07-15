def convert(n):
    ds = list(map(int, reversed(str(n))))
    return [sum(ds[::4]) - sum(ds[2::4]), sum(ds[1::4]) - sum(ds[3::4])]
