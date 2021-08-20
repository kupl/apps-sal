def luxhouse(houses):

    def f():
        m = 0
        for fl in reversed(houses):
            yield max(0, m - fl + 1)
            m = max(m, fl)
    return list(f())[::-1]
