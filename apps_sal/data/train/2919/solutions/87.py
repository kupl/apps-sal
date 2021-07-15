def encode(m, key):
    array_key = []
    list_int_str_key = [int(x) for x in str(key)]
    len_str_key = len(list_int_str_key)
    ords_list = [ord(x)-96 for x in m]
    len_ords_list = len(ords_list)
    i = 0
    while len(array_key) < len_ords_list:
        array_key.append(list_int_str_key[i])
        i += 1
        if i >= len_str_key: i = 0

    return [a+b for a,b in zip(array_key, ords_list)]
