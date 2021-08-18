def array_madness(a, b):
    a_list = 0
    b_list = 0
    for i in a:
        a_list = a_list + i**2
    for j in b:
        b_list = b_list + j ** 3
    if a_list > b_list:
        return True
    else:
        return False
