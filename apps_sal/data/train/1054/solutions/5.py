# cook your dish here
for i in range(int(input())):
    S=input()
    s=list(S)
    N=len(s)
    flag=True
    for i in range(N):
        if s[i]!=s[N-1-i] and s[i]!="." and s[N-1-i]!=".":
            flag=False
            print(-1)
            break
        elif s[i]=="." and s[N-1-i]==".":
            s[i]=s[N-1-i]="a"
        elif s[i]=="." and s[N-1-i]!=".":
            s[i]=s[N-1-i]
    
   
    
    if flag:
        p=""
        for i in s:
            p+=i
        print(p)
