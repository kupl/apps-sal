def product(s):
    return sum(1 for ch in s if ch == "!") * sum(1 for ch in s if ch == "?")
