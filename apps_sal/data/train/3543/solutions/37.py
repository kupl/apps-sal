
def increment_string(s):
    i, s2, n = 0, s[::-1], ''
    while True and i < len(s):
        if s2 and s2[i].isdigit():
            n += s2[i]
            i += 1
        else:
            break
    s, n = s[: len(s) - len(n)], int(n[::-1]) + 1 if n > '' else 1
    return s + str(n).zfill(i)
