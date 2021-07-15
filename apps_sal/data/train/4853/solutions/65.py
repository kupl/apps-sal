def double_char(s):
    lst=[]
    for x in s:
        lst.append(x)
        lst.append(x)
    lst = "".join(lst)
    return lst
