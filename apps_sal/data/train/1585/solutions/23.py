# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    if(a>b):
        print(a,a+b)
    elif(b>a):
        print(b,a+b)
