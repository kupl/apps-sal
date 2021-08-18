def dont_give_me_five(start, end):

    l = list(range(start, end + 1))
    new_l = []

    for i in l:
        if not '5' in str(i):
            new_l.append(i)
    return len(new_l)
