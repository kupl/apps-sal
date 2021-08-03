def count_sheep(n):
    store_1 = []
    for x in range(1, n + 1):
        store_1.append(f"{x} sheep...")
    my_lst_str = ''.join(map(str, store_1))
    return my_lst_str
