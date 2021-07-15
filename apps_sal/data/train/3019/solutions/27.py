def str_count(string, letter):
    res = 0
    for c in string.lower():
        res += 1 if c == letter else 0
    return res
