def hex_to_dec(s):
    hex_dict = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    hex_list = [i for i in s]
    pot_list = [i for i in range(0, len(hex_list))][::-1]
    res = 0
    for i in hex_list:
        if i in hex_dict:
            hex_list = [j.replace(i, str(hex_dict[i])) for j in hex_list]
    return sum([int(a) * (16**int(b)) for a, b in zip(hex_list, pot_list)])
