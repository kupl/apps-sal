# cook your dish here
n=int(input())
s=list(str(input()))
i=0
ans=0
while i<len(s)-1:
    if s[i]==s[i+1]:
        del s[i+1]
        ans+=1
    else:
        i+=1
print(ans)
