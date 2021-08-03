def super_size(n):
    n_list = (sorted([int(number) for number in str(n)], reverse=True))
    return int("".join(str(number) for number in n_list))
