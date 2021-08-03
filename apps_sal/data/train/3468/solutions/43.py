def scramble(s1, s2):
    s1_dict = {}
    for i in s1:
        if i in s1_dict:
            s1_dict[i] += 1
        else:
            s1_dict[i] = 1
    s2_dict = {}
    for i in s2:
        if i in s2_dict:
            s2_dict[i] += 1
        else:
            s2_dict[i] = 1
    for k, v in s2_dict.items():
        if k not in s1_dict or s1_dict[k] < v:
            return False
    return True
