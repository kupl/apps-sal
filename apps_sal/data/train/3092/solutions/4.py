def is_list(L):
    return type(L) == list


def is_index(I, size):
    return type(I) == int and 0 <= I < size


def is_char(C):
    return type(C) == str and len(C) == 1 and C.isalnum()


def is_tuple(size):
    return lambda T: type(T) == tuple and len(T) == 2 and is_index(T[0], size) and is_char(T[1])


def denumerate(enum_list):
    return is_list(enum_list) and all(map(is_tuple(len(enum_list)), enum_list)) and ''.join((t[1] for t in sorted(enum_list)))
