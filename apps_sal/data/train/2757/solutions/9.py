def check_password(s):
    import re
    chars = "!@
    sp = "[!@
    a = "[a-z]"
    if len(s) in range(8, 21):
        for c in s:
            if c not in chars:
                return "not valid"
    else:
        return "not valid"
    if all((re.search(sp, s), re.search("\d", s), re.search(a, s), re.search(a.upper(), s))):
        return "valid"
    else:
        return "not valid"
