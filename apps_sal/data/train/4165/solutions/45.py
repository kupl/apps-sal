def uni_total(string):
    unicodes = []
    for i in string:
        unicodes.append(ord(i))
    return sum(unicodes)
