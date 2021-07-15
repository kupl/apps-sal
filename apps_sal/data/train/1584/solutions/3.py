r,c,n=map(int,input().split())
ar=[]
for i in range(n):
    ar.append(list(map(int,input().split())))

d1={}


for i in ar:
    try:
        d1[i[0]]+=1
    except:
        d1[i[0]]=1

maxi=-1

for i in d1:
    if d1[i]>maxi:
        maxi=d1[i]
        res1=i

d2={}

for i in ar:
    if i[0]!=res1:
        try:
            d2[i[1]]+=1
        except:
            d2[i[1]]=1

maxi=-1

for i in d2:
    if d2[i]>maxi:
        maxi=d2[i]
        res2=i

ans1=d1[res1]+d2[res2]









d1={}

for i in ar:
    try:
        d1[i[1]]+=1
    except:
        d1[i[1]]=1

maxi=-1

for i in d1:
    if d1[i]>maxi:
        maxi=d1[i]
        res1=i

d2={}

for i in ar:
    if i[1]!=res1:
        try:
            d2[i[0]]+=1
        except:
            d2[i[0]]=1

maxi=-1

for i in d2:
    if d2[i]>maxi:
        maxi=d2[i]
        res2=i

ans2=d1[res1]+d2[res2]

print(max(ans1,ans2))
