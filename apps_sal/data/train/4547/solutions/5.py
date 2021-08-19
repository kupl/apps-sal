def more_zeros(s):
    al = []
    for char in s:
        bn = bin(ord(char))[2:]
        lbn = len(bn)
        if bn.count('0') > lbn / 2 and char not in al:
            al.append(char)
    return al
