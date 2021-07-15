def even_chars(st):
    lengthString=len(st)
    if lengthString<2 or lengthString>100:
        return "invalid string"
    else:
        list=[]
        for i in range(1,lengthString,2):
            list.append(st[i])
        return list
