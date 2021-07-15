def solve(s):
    UpperChars = 0
    LowerChars = 0

    for i in s:
        Checked_i = i.isupper()

        if Checked_i is True:
            UpperChars += 1
        else:
            LowerChars += 1

    if UpperChars > LowerChars:
        s = s.upper()
    elif LowerChars > UpperChars or LowerChars == UpperChars:
        s = s.lower()

    return s
