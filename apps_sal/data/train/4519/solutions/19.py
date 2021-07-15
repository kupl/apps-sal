def max_number(n):
    n_lst = [i for i in str(n)]
    n_lst.sort()
    n_lst.reverse()
    return int(''.join(n_lst))
