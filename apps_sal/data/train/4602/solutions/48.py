def is_anagram(a_str, b_str):
    if len(a_str) == len(b_str):
        a_list = list(a_str.lower())
        b_list = list(b_str.lower())
        for char in a_list:
            if char in b_list:
                b_list.remove(char)
        if not b_list:
            return True
        else:
            return False
    else:
        return False
