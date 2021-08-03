def first_dup(s):
    for i in [[s.count(i), i] for i in s]:
        if i[0] > 1:
            return i[1]
