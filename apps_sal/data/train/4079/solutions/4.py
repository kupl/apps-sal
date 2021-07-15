def encode(stg):
    return "".join(str(ord(c) - 96) if "a" <= c <= "z" else c for c in stg.lower())
