def compare(s1,s2):
    get_value = lambda string: sum(ord(char) for char in string.upper()) if string and string.isalpha() else 0
    return get_value(s1) == get_value(s2)
