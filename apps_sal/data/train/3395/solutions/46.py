def remove_duplicate_words(s):
    x=[s for s in s.split()]
    ans=[]
    for y in x:
        if y not in ans:
            ans.append(y)
    return "".join( x +" " for x in ans)[:-1]
