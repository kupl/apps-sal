def hamster_me(code, message):
    import string
    alpha = string.ascii_lowercase
    alplist = []
    clist = ""
    c = 0
    for x in message:
        while True:
            if alpha[alpha.index(x) - c] in code:
                clist += alpha[alpha.index(x) - c] + str(c + 1)
                c = 0
                break
            else:
                c += 1
    return clist
