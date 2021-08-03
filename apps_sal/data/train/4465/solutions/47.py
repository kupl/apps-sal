def super_size(n):
    n_str = str(n)
    str_sort = sorted(n_str, reverse=True)
    output = ""
    for num in str_sort:
        output = output + num
    return int(output)
