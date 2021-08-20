def dont_give_me_five(start, end):
    m = end - start + 1
    for i in range(start, end + 1):
        if '5' in str(i):
            m -= 1
    return m
