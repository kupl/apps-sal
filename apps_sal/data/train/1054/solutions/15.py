# cook your dish here
t=int(input())
for i in range(t):
    s=list(input())
    
    for j in range(len(s)):
        
            if(s[j]=='.'):
                if(s[len(s)-j-1]=='.'):
                    s[j]=s[len(s)-j-1]='a'
                else:
                    s[j]=s[len(s)-j-1]
            elif(s[len(s)-j-1]=='.'):
                if(s[j]=='.'):
                    s[j]=s[len(s)-j-1]='a'
                else:
                    s[len(s)-j-1]=s[j]
            
            
            
                
            if(len(s)%2!=0):
                if(j==((len(s)//2))):
                
                    if(s[j]=='.'):
                        s[j]="a"
    c=""
    m=""
    flag=1
    c=list(c.join(s))
    for k in range(len(c)//2):
        if(c[k]==c[len(c)-k-1]):
            flag=0
            
            
        else:
            flag=1
            break
    if(flag==0):
        print(m.join(c))
    else:
        print(-1)
    
    
