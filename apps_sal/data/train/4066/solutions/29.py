def string_to_array(s):
    # your code here
    l = []
    if(s == ""):
        l.append("")
        return l
    else:
        for i in s.split():
            l.append(i)
        return l
