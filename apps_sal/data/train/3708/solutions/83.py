def hex_to_dec(s):
    number = 0
    lst = list(s)
    lst.reverse()
    for n in range(len(lst)):
        lst[n] = ord(lst[n]) - 87 if ord(lst[n]) > 96 else lst[n]
        number += int(lst[n]) * 16 ** n
    return number
