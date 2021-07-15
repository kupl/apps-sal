# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l=[ i for i in range(len(l)) if l[i] == 1 ]
    social_distance=True
    for i in range(1,len(l)):
        if l[i]-l[i-1]<6:
            social_distance=False
    if social_distance==False:
        print('NO')
    else:
        print('YES')
    
