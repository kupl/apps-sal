def evenator(s):
    return " ".join([w+w[-1] if len(w)&1 else w for w in "".join([c for c in s if c.isalnum() or c == " "]).split()])
