def hex_to_dec(s):
    index = []
    for n in range(len(s)):
        index.append(s[n:n + 1])
    i_len = len(index)
    index = [10 if x == 'a' else x for x in index]
    index = [11 if x == 'b' else x for x in index]
    index = [12 if x == 'c' else x for x in index]
    index = [13 if x == 'd' else x for x in index]
    index = [14 if x == 'e' else x for x in index]
    index = [15 if x == 'f' else x for x in index]
    o = len(index)
    sum_dec = 0
    for i in range(i_len):
        sum_dec += int(index[i]) * 16**(o - 1)
        o -= 1
    return sum_dec


hex_to_dec("a1b2")
