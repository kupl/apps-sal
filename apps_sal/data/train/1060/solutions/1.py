# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    c=0
    count01=[[0,0] for _ in range(n)]
    for i in range(n-2,-1,-1):
        if s[i+1]=='1':
            count01[i][1]=count01[i+1][1]+1
            count01[i][0]=count01[i+1][0]
        else:
            count01[i][0]=count01[i+1][0]+1
            count01[i][1]=count01[i+1][1]
    for i in range(n):
        if s[i]=='1':
            c+=count01[i][0]
        else:
            c+=count01[i][1]
        # print("i=",i)
        # print(c)
        # print(count01)
    print(c)
