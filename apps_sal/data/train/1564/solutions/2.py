t=int(eval(input()))
while t:
    a=[]
    t=t-1
    s=input()
    a.append(s[:2])
    for i in range(1,len(s)-1):
        c=s[i:i+2]
        if c not in a:
            a.append(c)
    print(str(len(a)))
    
