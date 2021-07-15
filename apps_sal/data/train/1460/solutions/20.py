# cook your dish here
d,x,y=[int(i) for i in list(input().split())]
l=[int(i) for i in list(input().split())]
sav=d*x
dec=(y*2)/100
for i in range(0,d):
    temp=y
    for j in range(1,l[i]):
        temp-=dec
        dec=(temp*2)/100
    sav+=temp
if sav>=300:
    print('YES')
else:
    print("NO")
    

