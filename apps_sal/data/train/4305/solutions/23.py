def order_weight(strng):
    my_list = sorted([int(i) for i in strng.split()], key=lambda x: str(x))
    sorted_int_list = sorted(my_list, key=lambda x: sum((int(d) for d in str(x))))
    return ' '.join(map(str, sorted_int_list))
