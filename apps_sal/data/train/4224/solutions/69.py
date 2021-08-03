def dont_give_me_five(start, end):

    end = end + 1
    nofives = 0
    for i in range(start, end):
        if '5' not in str(i):
            nofives += 1
        else:
            pass
    return nofives
