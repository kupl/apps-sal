def super_size(n):
    num = [int(x) for x in str(n)]
    num.sort(reverse=True)
    num_str = [str(x) for x in num]
    big_num_str = ''.join(num_str)
    return int(big_num_str)
