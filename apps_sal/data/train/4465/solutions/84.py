def super_size(n):
    n_list = list(str(n))
    n_list.sort(reverse=True)
    n_string = ''.join(n_list)
    return int(n_string)

