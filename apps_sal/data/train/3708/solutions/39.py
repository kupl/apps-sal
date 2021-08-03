def hex_to_dec(s):
    hexn = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    sum = 0
    n = 0
    for i in s[::-1]:
        if i.upper() in hexn:
            sum += hexn[i.upper()] * 16**n
        else:
            sum += int(i) * 16**n
        n += 1
    return sum
