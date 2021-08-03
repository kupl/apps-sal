def uni_total(string):
    a = list(string)
    tot = 0
    for i in a:
        tot = tot + ord(i)
    return(tot)
