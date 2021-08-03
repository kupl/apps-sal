def remove_duplicate_words(s):
    list = s.split()
    new = []
    for x in list:
        if x not in new and new.count(x) == 0:
            new.append(x)
    s = " "
    return (s.join(new))
