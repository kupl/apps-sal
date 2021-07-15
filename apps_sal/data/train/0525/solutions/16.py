a=int(input())
for i in range(a):
    l=list(map(int,input().split()))
    for i in range(((l[2]-l[1])//l[0])+1):
        x=(i*l[0])+l[1]
        while(x>=l[2]):
            break
    print(x)
