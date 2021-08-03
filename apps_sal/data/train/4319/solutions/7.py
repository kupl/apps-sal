def countzero(string):
    n = 0
    for i in string:
        if i in "069abdeopqDOPQRg(":
            n += 1
        elif i in "8%&B":
            n += 2

    return n
