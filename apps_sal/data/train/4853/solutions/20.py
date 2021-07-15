def double_char(s):
    new_s = ""
    for c in s:
        new_s = "%s%c%c" % (new_s, c, c);
    return new_s
