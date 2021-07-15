def str_count(strng, letter):
    res = 0
    for simv in strng:
        if simv is letter:
            res = res + 1
    return res
