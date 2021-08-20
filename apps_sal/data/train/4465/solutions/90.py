def super_size(n):
    n_str = str(n)
    n_sorted = sorted(n_str, reverse=True)
    sorted_str = ''
    for i in n_sorted:
        sorted_str += i
    return int(sorted_str)
