def scramble(stg, lst):
    return "".join(t[1] for t in sorted(enumerate(stg), key=lambda t: lst[t[0]]))
