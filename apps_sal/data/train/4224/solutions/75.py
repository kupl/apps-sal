def dont_give_me_five(start, end):

    c = 0

    for i in range(start, end + 1):

        d = [int(x) for x in str(abs(i))]

        if not 5 in d:

            c += 1

    return c
