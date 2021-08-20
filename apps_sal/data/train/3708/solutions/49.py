def hex_to_dec(s):
    hex_dict = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    temp = list(map(hex_dict.index, s))
    pow = range(len(s) - 1, -1, -1)
    return sum((temp[i] * 16 ** pow[i] for i in range(len(s))))
