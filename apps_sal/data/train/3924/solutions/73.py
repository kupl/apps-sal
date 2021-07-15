def reverse_words(text):
    t = text.split()
    t_new = []
    for i in t:
        i = i[::-1]
        t_new.append(i)
    sp1 = " ".join(t_new)
    if len(sp1) != len(text):
        sp2 = "  ".join(t_new)
        return sp2
    else:
        return sp1
