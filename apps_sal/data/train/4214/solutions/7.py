def spin_solve(sentence):
    s = ''
    w = ''
    for ot in sentence:
        if ot.isalpha() or ot in "'-'":
            w += ot
        else:
            if len(w) > 6 or w.upper().count("T") > 1:
                s += w[::-1]
            elif len(w) == 2 or ot == ',':
                s += w.upper()
            elif len(w) == 1:
                s += "0"
            else:
                s += w
            w = ''
            s += ot
    return s
