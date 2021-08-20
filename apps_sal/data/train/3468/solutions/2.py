def scramble(s1, s2):
    return not any((s1.count(char) < s2.count(char) for char in set(s2)))
