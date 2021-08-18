def increment_string(s):
    num = ''
    for c in reversed(s):
        if c.isdigit():
            num += c
            s = s[:-1]
        else:
            break

    if not num:
        return s + '1'

    fmt = "0{}d".format(len(num))
    return s + format(int(num[::-1]) + 1, fmt)
