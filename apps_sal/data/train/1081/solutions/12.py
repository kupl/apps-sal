n=int(input())
l=[98, 57, 31, 45, 46 ]
a='abcdefghijklmnopqrstuvwxyz' 

for i in range(n):
    s=input().strip().lower()
    ans='' 
    c=0
    for j in s:
        k=a.index(j)+l[c] 
        c+=1 
        k=k%26 
        ans+=a[k] 
    print(ans.upper())
