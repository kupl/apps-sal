# cook your dish here
for _ in range(0,int(input())):
    s=input()
    c=0
    ans=0
    for i in range(0,len(s)):
        if s[i]=="<":
            c=c+1
        else:
            c=c-1
        if c==0:
            ans=i+1
        elif c<0:
            break
    print(ans)
        
