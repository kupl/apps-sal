def hex_to_dec(s):
    hex_dic = {}

    for i in range(10):
        hex_dic[str(i)] = i

    next_letter = 10
    for i in ['a', 'b', 'c', 'd', 'e', 'f']:
        hex_dic[i] = next_letter
        next_letter += 1

    base = 16
    num_digits = len(s) - 1
    dec_val = 0
    pos = 0

    for i in range(num_digits, -1, -1):
        dec_val += hex_dic[s[pos]] * base**i
        pos += 1

    return dec_val
