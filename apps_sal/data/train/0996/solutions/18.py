t=int(input())
l1=0
l2=0
s1=0
s2=0
for i in range(t):
    ss1,ss2=list(map(int,input().split()))
    s1+=ss1
    s2+=ss2
    if s1-s2<0:
        if s2-s1>=l2:
            l2=s2-s1
    else:
        if s1-s2>=l1:
            l1=s1-s2
if l1>l2:
    print(1,l1)
else:
    print(2,l2)

