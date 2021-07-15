def digits(n):
    n_str = str(n)
    n_list = n_str.split('.')
    count = len(n_list[0])
    return count
