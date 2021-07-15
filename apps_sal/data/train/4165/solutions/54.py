def uni_total(string):
    b = []
    for i in range(len(string)):
        b.append(ord(string[i]))
    return sum(b)
