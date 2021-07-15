def string_letter_count(s):
    s = s.lower()
    m = ''
    for i in sorted(list(set(s))):
        if i.islower():
            m += str(s.count(i)) + i
    return m
