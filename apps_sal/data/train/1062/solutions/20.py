def replace(l,key,i,j):
    for k in range(i,j+1):
        l[k]=str(key)
n=int(input())
s=str(n)
i=0
j=n*2-2
key=n
m=[]
l=((n*2)-1)*s.split()
for i in range(int((n*2-2)/2)+1):
    replace(l,key,i,j)
    key-=1
    j-=1
    m.append(' '.join(l))
for j in range(n-2,-1,-1):
    m.append(m[j])
for p in m:
    print(p)
    

                       
                       

