def max_number(n):
    n_list = [ch for ch in str(n)]
    n_list.sort(reverse=True)
    return int("".join(n_list))
