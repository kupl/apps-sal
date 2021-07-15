def remove_exclamation_marks(s):
    s = list(s)
    x = 0
    for element in s:
        while True:
            if (len(s) == x):
                break
            if (s[x] == "!"):
                del s[x]
            else:
                break
        x += 1
    s = ''.join(s)
    return s
