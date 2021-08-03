def evenator(s):
    words = [dupiword(evenatorword(s)) for s in s.split(" ")]
    return " ".join(words).strip()


def dupiword(s):
    return s + s[len(s) - 1] if len(s) % 2 else s


def evenatorword(w):
    return "".join([x if x.isalnum() else '' for x in w]).replace("  ", " ")
