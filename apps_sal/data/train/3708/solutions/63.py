def hex_to_dec(s):
    hex_num = '0123456789abcdef'
    count = 0
    decimal_num = 0
    for i in s[::-1]:
        decimal_num += hex_num.index(i) * 16 ** count
        count += 1
    return decimal_num
