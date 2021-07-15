def increment_string(s):
    if s and s[-1].isdigit():
        return increment_string(s[:-1]) + "0" if s[-1] == "9" else s[:-1] + repr(int(s[-1]) + 1)
    return s + "1"

