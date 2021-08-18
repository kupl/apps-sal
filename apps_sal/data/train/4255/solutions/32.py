def make_upper_case(s):
    res = ""
    for char in s:
        if char.islower():
            key = chr(ord(char) - 32)
            res = res + key
        else:
            res = res + char
    return res
