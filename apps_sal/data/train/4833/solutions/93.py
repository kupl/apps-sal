def replace_exclamation(s):
    s = list(s)
    for char in s:
        if char.lower() in "aeiou":
            s[s.index(char)] = "!"
    return "".join(s)
