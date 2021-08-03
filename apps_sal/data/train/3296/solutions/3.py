def what_century(year):
    def ordinal(n): return "%d%s" % (n, "tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])
    return ordinal((int(year) - 1) // 100 + 1)
