def scramble(s1, s2):
    s1_dict = dict()
    for char in s1:
        if char in s1_dict:
            s1_dict[char] = s1_dict[char] + 1
        else:
            s1_dict[char] = 1
    for char in s2:
        if char not in s1_dict or s1_dict[char] == 0:
            return False
        else:
            s1_dict[char] = s1_dict[char] - 1
    return True
