def hex_word_sum(string, res = 0):
    s = string.replace('O', '0').replace('S', '5').split()

    for i in s:
        try:
            res += int(i, 16)
        except: pass

    return res
