n=int(input())
l=[int(x) for x in input().split()]
fr=0
to=0
r=1
for i in range(0,len(l)):
    if(l[i]==r):
        r+=1
    else:
        fr=r
        to=l[i]
        break
dup=to
br=0
for i in range(fr-1,to):
    if(l[i]==dup):
        dup-=1
    else:
        br=1
        break
dup=to+1
for i in range(to,len(l)):
    if(br==1):
        break
    if(l[i]==dup):
        dup+=1
    else:
        br=1
if(br==1):
    print("0 0")
else:
    print(fr,to)
        
    

