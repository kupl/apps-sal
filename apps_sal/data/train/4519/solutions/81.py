def max_number(n):
    new_list = []
    n = str(n)
    for x in n:
        new_list.append(x)
    new_list = sorted(new_list, reverse=True)
    return int(''.join(new_list))
