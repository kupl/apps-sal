def string_clean(s):
    l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in l:
        if i in s:
            s = s.replace(i, "")
    return s
