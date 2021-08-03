def convert_to_dms(*args):
    lst = []
    for i, v in enumerate(map(float, args)):
        av = abs(v)
        d = int(av)
        m = int((av - d) * 60)
        s = (av - d - m / 60) * 3600
        lst.append("{:03}*{:02}'{:06.3f}\"{}".format(d, m, s, ["NS", "EW"][i][v < 0]))
    return tuple(lst)
