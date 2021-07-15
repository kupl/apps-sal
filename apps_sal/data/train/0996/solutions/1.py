s1=s2=lead=0
mlead1=mlead2=0
for _ in range(int(input())):
    x, y= list(map(int, input().split()))
    s1, s2= s1+x, s2+y
    if(s1>s2):
        lead=(s1-s2)
        mlead1= max(mlead1, lead)
    else:
        lead=(s1-s2)
        mlead2= min(mlead2, lead)
if(mlead1<(-mlead2)):
    print('2', -mlead2)
else:
    print('1', mlead1)


