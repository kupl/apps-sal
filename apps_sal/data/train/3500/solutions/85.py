def remove_exclamation_marks(s):
    a = s.strip("!")
    l = []
    for i in range(0, len(a)):
        s = a[i]
        l.append(s)
    while "!" in l:
        l.pop(l.index("!"))
    return "".join(l)
