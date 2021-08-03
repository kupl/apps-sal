def create_phone_number(n):
    n = "".join([str(x) for x in n])
    return("(" + str(n[0:3]) + ")" + " " + str(n[3:6]) + "-" + str(n[6:]))
