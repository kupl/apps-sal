def alan_annoying_kid(s):
    a = s[:-1].split()
    b = f"did {a[3]} it" if a[2] == "didn't" else f"didn't {a[2][:-2]} at all"
    return f"I don't think you {' '.join(a[2:])} today, I think you {b}!"
