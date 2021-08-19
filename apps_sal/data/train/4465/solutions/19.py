def super_size(n):
    num_str = list(str(n))
    num_str.sort(reverse=True)
    res = int(''.join(num_str))
    return res
