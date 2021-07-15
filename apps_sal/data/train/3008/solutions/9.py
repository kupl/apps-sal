def sort_array(value):
    lst=[]
    str= ""
    for i in value:
        lst.append(i)
        lst.sort()
    for a in lst:
        str+=a
    return str
