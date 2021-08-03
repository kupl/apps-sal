def super_size(n):
    n_str = str(n)
    n_sorted = sorted(n_str, reverse=True)
    n_joined = ''

    for i in n_sorted:
        n_joined += i

    n_reverse = int(n_joined)
    return n_reverse
