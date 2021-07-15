from collections import Counter 
for _ in range(int(input())):
    n=int(input())
    s=input()
    t=input()
    c1=Counter(s)
    c2=Counter(t)
    if  c1!=c2:
        print('NO')
        continue 
    if n>26:
        print('YES')
        continue 
    if max(c1.values())>=2:
        print("YES")
        continue
    p1=0 
    p2=0 
    for i in range(n):
        for j in range(i+1,n):
            if s[i]>s[j]:
                p1+=1 
            if t[i]>t[j]:
                p2+=1 
    print('YES' if p1%2==p2%2 else "NO")
