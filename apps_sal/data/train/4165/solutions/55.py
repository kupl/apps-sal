def uni_total(string):
    if not string:
        return 0
    if len(string) == 1:
        return ord(string)
    return sum(list(map(ord, string)))
