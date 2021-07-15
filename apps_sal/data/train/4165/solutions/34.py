def uni_total(string):
    total = 0
    if string == "":
        return 0
    else:
        for i in range(len(string)):
             total = ord(string[i]) + total
    return total
