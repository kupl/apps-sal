def super_size(n):
    n_str = str(n)
    n_sorted = sorted(n_str, reverse=True)
    output_str = ""
    for num in n_sorted:
        output_str = output_str + num
    if n_str == n_sorted:
        return int(n_str)
    else:
        return int(output_str)
