def sorter(textbooks):
    a = [i.lower() for i in textbooks]
    s = sorted(a)
    for i in range(len(s)):
        if s[i] in textbooks:
            pass
        else:
            s[i] = textbooks[a.index(s[i])]
    return s
