def scramble(s1, s2):
    return len([x for x in [(char, s2.count(char), s1.count(char)) for char in set(s2)] if x[2] < x[1]]) == 0
