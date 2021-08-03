def increment_string(s):
    b = []
    if s and s[-1].isdigit():
        for c in reversed(s):
            if c.isdigit():
                b.append(c)
            else:
                break
        return s[:-len(b)] + str(int("".join(reversed(b))) + 1).zfill(len(b))
    return s + "1"
