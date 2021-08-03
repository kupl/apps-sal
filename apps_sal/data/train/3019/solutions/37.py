def str_count(string, letter):
    res = 0
    for i in string:
        if i == letter:
            res += 1
    return res
