def reverse(s):
    s=list(s)
    indexes=[]
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            indexes.append(i)
            indexes.append(i+1)
    for i in list(set(indexes)):
        s[i]=s[i].swapcase()
    return "".join(s)
        

