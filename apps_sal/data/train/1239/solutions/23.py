t=int(input())
for i in range(t):
    n=int(input())
    ans=[]
    meow=''
    tot = n+1
    for i in range(n,-1,-1):
        meow+=str(i)
        an=" "*(tot-len(str(meow)))+str(meow)
        ans.append(an)
    for j in ans:
        print(j)
    ans=list(reversed(ans))
    ans.pop(0)
    for j in ans:
        print(j)
