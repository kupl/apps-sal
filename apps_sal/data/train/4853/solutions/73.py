def double_char(s):
    double = ""
    for i in range(len(s)):
        double += "{}".format(s[i] * 2)
    return double


double_char("String")
