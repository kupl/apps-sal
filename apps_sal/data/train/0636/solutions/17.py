# cook your dish here
a = list(map(int,input("").strip().split()))   
n=a[0];
t=a[1];
del a[0]
del a[0]
a.sort()
res=list()
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            for l in range(k+1,n):
                if a[i]+a[j]+a[k]+a[l]==t:
                    li=list();
                    li.append(i)
                    li.append(j)
                    li.append(k)
                    li.append(l)
                    if li not in res:
                        res.append(li)
                elif a[i]+a[j]+a[k]+a[l]>t:
                    break;
                
print(len(res))
