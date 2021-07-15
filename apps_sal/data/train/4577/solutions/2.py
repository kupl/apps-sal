def debug(s):
    s=s.replace("bugs", "^")
    s=s.replace("bug", "")
    s=s.replace("^", "bugs")
    return s
