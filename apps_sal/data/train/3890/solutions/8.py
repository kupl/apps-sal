def get_honor_path(s, o):
    return o > s and {'%skyus' % k: n for (k, n) in enumerate(divmod(o - s, 2), 1)} or {}
