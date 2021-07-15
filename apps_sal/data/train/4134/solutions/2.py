from math import ceil


def cooking_time(n_pow, n_min, n_sec, pow):
    m, s = divmod(ceil((60 * n_min + n_sec) * int(n_pow[:-1]) / int(pow[:-1])), 60)
    return f"{m} minutes {s} seconds"
