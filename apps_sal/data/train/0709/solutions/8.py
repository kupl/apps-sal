# cook your dish here
for i in range(int(input())):
    n=input()
    l=list(map(int,input().split()))
    m=l[0];x=l[-1]
    print(max(m,x))
