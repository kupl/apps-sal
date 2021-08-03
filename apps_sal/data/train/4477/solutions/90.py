def reverse_number(n):
    lst = [x for x in list(str(n))]
    lst.reverse()

    if n > -1:
        result = int("".join(lst))

    else:
        result = int("".join(lst[:-1])) * -1

    return result
