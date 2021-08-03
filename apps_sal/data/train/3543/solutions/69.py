def increment_string(strng):
    if strng == "":
        return "1"
    if not strng[-1].isdigit():
        strng += "1"
    else:
        c = ""
        ll = len(strng) - 1
        while strng[ll].isdigit():
            c = strng[ll] + c
            ll -= 1
            if ll < 0:
                break
        lenc = len(c)
        c = str(int(c) + 1)
        if len(c) < lenc:
            c = "0" * (lenc - len(c)) + c
        strng = strng[:ll + 1] + c
    return strng
