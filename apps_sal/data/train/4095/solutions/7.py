def added_char(s1, s2):
    return next((i for i in s2 if s1.count(i) != s2.count(i)))
