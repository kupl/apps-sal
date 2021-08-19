def hex_to_dec(s):
    ords = [ord(x) for x in s]
    ints = [x - 48 if x < 90 else x - 87 for x in ords]
    res = 0
    for i in range(len(s)):
        curr_power = len(s) - 1 - i
        res += ints[i] * 16 ** curr_power
    return res
