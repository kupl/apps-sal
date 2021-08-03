def uni_total(string):
    return 0 if len(string) == 0 else sum([int(ord(ch)) for ch in string])
