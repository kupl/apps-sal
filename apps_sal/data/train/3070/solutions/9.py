def unique_sum(lst):

    if lst == []:

        return None

    else:

        s = set(lst)

        v = list(s)

        d = sum(v)

        return d
