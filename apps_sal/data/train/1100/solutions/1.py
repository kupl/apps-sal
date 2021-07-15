# cook your dish here
for _ in range(int(input())):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    cnt=0
    if (b[0]-a[0]<0 or b[1]-a[1]<0 or b[2]-a[2]<0):
        print(-1)
    else:
        if(a==b):
            print(0)
        else:
            for i in range(3):
                if b[i]-a[i]!=0:
                    cnt+=b[i]-a[i];
            print(cnt)       
