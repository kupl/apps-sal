def dig_pow(n, p):
    n_list = [int(i) for i in str(n)]
    n_sum = 0
    p_i = p
    for n_i in n_list:
        n_sum = n_sum + n_i**p_i
        p_i = p_i + 1
    if n_sum % n == 0:
        return n_sum / n
    else:
        return -1
