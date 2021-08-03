def dont_give_me_five(start, end):

    n = 0
    for x in range(start, end + 1):
        if '5' in str(x):
            continue
        n = n + 1
    return n
