def sort_string(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rule12 = list(sorted([x for x in s if x.lower() in alphabet], key=lambda i: alphabet.find(i.lower())))
    for i, sym in enumerate(s):
        if sym.lower() not in alphabet:
            rule12.insert(i, sym)
    return "".join(rule12)

