def buy_newspaper(s1,s2):
    if [1 for i in s2 if i not in s1]: return -1
    p=0    
    for i in s2:
        while i!=s1[p%len(s1)]:
            p+=1
        p+=1
    return p//len(s1)+(1 if p%len(s1) else 0)
