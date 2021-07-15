def capitalize(s):
    even = "".join(w.upper() if i%2 else w.lower() for i,w in enumerate(s))
    odd = "".join(w.lower() if i%2 else w.upper() for i,w in enumerate(s))
    return [odd, even]
