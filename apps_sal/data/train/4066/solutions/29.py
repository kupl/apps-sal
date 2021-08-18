def string_to_array(s):
    l = []
    if(s == ""):
        l.append("")
        return l
    else:
        for i in s.split():
            l.append(i)
        return l
