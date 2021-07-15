t=int(input())
while t:
    s=input()
    ans=0
    temp=0
    for i in range(len(s)):
        if(s[i]=='L'):
            temp+=1
        else:
            ans=max(ans,temp+1)
            temp=0
    ans=max(ans,temp+1)  
    print(ans)
    t-=1
