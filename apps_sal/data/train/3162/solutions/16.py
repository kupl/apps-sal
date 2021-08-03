def compare(s1, s2):
    def get_value(string): return sum(ord(char) for char in string.upper()) if string and string.isalpha() else 0
    return get_value(s1) == get_value(s2)
