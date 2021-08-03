def scramble(s1, s2):
    if len(s1) < len(s2):
        return False
    s1_dict = {}
    s2_dict = {}
    for char in s1:
        try:
            s1_dict[char] += 1
        except KeyError:
            s1_dict[char] = 1
    for char in s2:
        try:
            s2_dict[char] += 1
        except KeyError:
            s2_dict[char] = 1
    for key in s2_dict:
        try:
            if s1_dict[key] < s2_dict[key]:
                return False
        except KeyError:
            return False
    return True
