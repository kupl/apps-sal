def double_char(s):
    s=list(s)
    lists=[]
    for i in range(len(s)):
        lists.append(s[i]*2)
    string=''
    for i in range(len(lists)):
        string=string+lists[i]
    return string

