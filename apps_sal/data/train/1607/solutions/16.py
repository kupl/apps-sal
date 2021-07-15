s=input()
n=len(s)
ans=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if s[i]=='Q' and s[j]=='A' and s[k]=='Q':
                ans+=1
print(ans)
