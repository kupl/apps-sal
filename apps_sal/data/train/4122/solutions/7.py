def sc(s):
    for i in s:
        if i.islower()==True:
            if i.upper() not in s:
                s=s.replace(i,'')
        else:
            if i.lower() not in s:
                s=s.replace(i,'')
    return s
