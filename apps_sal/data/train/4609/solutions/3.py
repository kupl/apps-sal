def egged(year, span):
    def eggs(e, n): return 0 if n == 0 else e + eggs(int(e * .8), n - 1)
    return eggs(300, min(year, span)) * 3 if year else 'No chickens yet!'
