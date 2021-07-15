def compare(s1,s2):
    a1,a2=0,0
    if s1!=None and s1!='':    
        for i in s1:
            if not i.isalpha():
                a1=0
                break
            else:
                a1+=ord(i.upper())
    if s2!=None or s2!='':
        for j in s2:
            if not j.isalpha():
                a2=0
                break
            else:
                a2+=ord(j.upper())
    return a1==a2
