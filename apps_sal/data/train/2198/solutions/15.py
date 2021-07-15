c=[]
n=int(input())
for uygf in range(n):
    s=list(input())
    l=len(s)
    i=0
    p=[]
    d=['u','o','k','h']
    while(i<l):
        if(s[i] not in d):
            p.append(s[i])
            i+=1
        elif(s[i]=='o'):
            if(i+1<l and s[i+1]=='o'):
                p.append('u')
                i+=2
            elif(i+1<l and s[i+1]=='u'):
                p.append('u')
                s[i+1]='o'
                i+=1
            else:
                p.append('o')
                i+=1
        elif(s[i]=='k'):
            y=i+1
            while(y<l and s[y]=='k'):
                y+=1
            if(y!=l):
                if(s[y]=='h'):

                    p.append('h')
                    i=y+1
                else:
                    for pp in range(i,y):
                        p.append('k')
                    i=y
            else:
                for pp in range(i,y):
                    p.append('k')
                i=y
        else:
            p.append(s[i])
            i+=1

    c.append(p)
d=[]
for i in range(n):
    if(i in d):
        continue
    for j in range(i+1,n):
        if(c[i]==c[j]):
            d.append(j)
print(n-len(d))



