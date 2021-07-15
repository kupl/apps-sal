# cook your dish here
a=int(input())
for i in range(a):
    count=0
    num=int(input())
    w=num/2
    b=[]
    b=input().split()
    for i in range(len(b)):
        b[i]=int(b[i])
    for i in b:
        if(i>=w):
            count+=1
    print(count)

