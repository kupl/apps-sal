def trigrams(p):
    r = ""
    for i in range(len(p) - 2):
        r += p[i:i + 3].replace(" ", "_") + " "
    return r.strip()
