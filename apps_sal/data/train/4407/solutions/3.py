def no_ifs_no_buts(a, b):
    while a<b:
        return str(a) + " is smaller than " + str(b)
    while a>b:
        return str(a) + " is greater than " + str(b)
    while a==b:
        return str(a) + " is equal to " + str(b)
