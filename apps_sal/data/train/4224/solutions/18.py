def dont_give_me_five(start, end):
    n_list = [i for i in range(start, end + 1)]
    n = 0
    for i in n_list:
        if '5' in str(i):
            continue
        n += 1
    return n   # amount of numbers
