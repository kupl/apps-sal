q=input()
a,s=[],[]
for i in range(0,len(q)):
    if q[i]=='Q':
        a.append(i)
    elif q[i]=='A':
        s.append(i)
ans=0
for i in a:
    h=list([x for x in s if x>i])
    for j in h:
        ans+=len(list([y for y in a if y>j]))
print(ans)

