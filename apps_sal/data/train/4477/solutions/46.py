def reverse_number(n):
    if str(n)[0] == "-":
        return int("-{}".format(str(n)[1:][::-1]))
    elif n == 0:
        return 0
    else:
        return int(str(n)[::-1].lstrip("0"))
