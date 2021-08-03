def is_keith_number(n):
    if n <= 10:
        return False
    c, k_lst, k_num = 0, list(str(n)), n
    while k_num <= n:
        k_num = sum([int(x) for x in k_lst])
        c += 1
        if k_num == n:
            return c
        k_lst.append(k_num)
        k_lst.pop(0)
    return False
