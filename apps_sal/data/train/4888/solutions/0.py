def recaman(n):
    series, last = {0}, 0
    for i in range(1, n + 1):
        test = last - i
        last = last + i if test < 0 or test in series else test
        series.add(last)

    return last
