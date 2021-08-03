def divisors(integer):

    lst = []
    for i in range(2, integer):
        if integer % i == 0:
            lst.append(i)

    if len(lst) == 0:
        return "%s is prime" % (integer)
    else:
        return lst
