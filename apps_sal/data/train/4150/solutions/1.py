def rot13(message):
    PAIRS = dict(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"))
    return "".join(PAIRS.get(c, c) for c in message)
