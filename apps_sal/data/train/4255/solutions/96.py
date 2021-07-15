def make_upper_case(s):
    word_upper_case = ""
    for c in s:
        if 97 <= ord(c) <= 122:
            word_upper_case += chr(ord(c) - 32)
        else:
            word_upper_case += c
    return word_upper_case
