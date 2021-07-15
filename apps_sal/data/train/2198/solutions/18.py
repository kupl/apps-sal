n=int(input())
l=[]
for i in range(n):
    l.append(list(input().strip()))
ans=1
for i in range(n):
    j=len(l[i])-1
    if (len(l[i])==1):
        if (l[i][0]=='u'):
            l[i]=['o','o']
        else:
            continue
    while (j>0):
        if (l[i][j]=='h' and l[i][j-1]=='k'):
            l[i][j-1:j+1]=['h']
        j-=1
    j=0
    while (True):
        try:
            if (l[i][j]=='u'):
                l[i][j:j+1]=['o','o']
                j+=1
        except:
            break
        j+=1
l.sort()
for i in range(n-1):
    if (l[i]!=l[i+1]):
        ans+=1
print (ans)
