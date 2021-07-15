def compare(s1,s2):
    #your code here
    if s1 == None:
        s1 = ""
    if s2 == None:
        s2 =""
    s1 = s1.upper()
    s2 = s2.upper()
    c1 = 0
    c2 = 0
    for i in s1:
        if not i.isalpha():
            c1=0
            break
        c1+= ord(i)
    
    for i in s2:
        if not i.isalpha():
            c2=0
            break
        c2+= ord(i)
    return c1 == c2
