t=eval(input())

while t>0:
    a=[[0 for x in range(26)] for x in range(26)]
    ans=0
    t-=1
    s=list(input())
    for i in range(len(s)-1):
        #print s[i]
        if a[ord(s[i])-65][ord(s[i+1])-65]==0:
            #print s[i],"hello"
            a[ord(s[i])-65][ord(s[i+1])-65]=1
            ans+=1
    print(ans)

