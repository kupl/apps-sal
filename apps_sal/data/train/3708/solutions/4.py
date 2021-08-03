def hex_to_dec(s):
    hxdict = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    count = 0
    total = 0
    for num in reversed(s):
        if num.isalpha():
            hxnum = hxdict.get(num)
            total = total + hxnum * (16**count)
            count += 1
        else:
            total = int(num) * (16**count) + total
            count += 1
    return total
