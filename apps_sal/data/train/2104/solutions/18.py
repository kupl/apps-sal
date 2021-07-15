n=int(input())
s=sorted(list(map(int,input().split())))
ans=(s[n-1]-s[0])*(s[2*n-1]-s[n])
for i in range(n):ans=min(ans,(s[2*n-1]-s[0])*(s[n-1+i]-s[i]))
print(ans)

