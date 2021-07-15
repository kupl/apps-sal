def grille(message, code):
    l = len(message)
    return "".join(c for c, b in zip(message, f"{code:{l}b}"[-l:]) if b == "1")
