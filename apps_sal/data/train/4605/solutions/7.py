def replace_dashes_as_one(s):
    res = ""
    i = 0
    while i < len(s):
        if s[i] != "-":
            res += s[i]
            i += 1
        else:
            res += "-"
            j = i + 1
            while j < len(s) and (s[j] == " " or s[j] == "-"):
                j += 1
            i = j
            if i < len(s) and s[i] != "-" and s[i - 1] == " ":
                res += " "
    return res + " " if s[-1] == " " else res
