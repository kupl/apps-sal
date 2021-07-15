def super_size(n):
    n_list = [i for i in str(n)]
    n_list.sort(reverse=True)
    return int("".join(n_list))
