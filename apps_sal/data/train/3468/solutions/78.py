def scramble(s1, s2):
    dict_s1 = {}
    for char in s1:
        dict_s1[char] = dict_s1[char] + 1 if char in dict_s1.keys() else 1
    for char in set(s2):
        if not char in dict_s1.keys():
            return False
        if s2.count(char) > dict_s1[char]:
            return False
        dict_s1[char] -= s2.count(char)
    return True
