def  lowercase_count(strg):
    c=0
    case = "abcdefghijklmnopqrstuvwxyz"
    for x in strg:
        if x in case:
            c = c +1
    return c
