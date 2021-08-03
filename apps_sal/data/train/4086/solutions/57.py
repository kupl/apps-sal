def first_non_consecutive(x):

    for i in x:
        if i - 1 not in x:
            if i == x[0]:
                pass
            else:
                return i
