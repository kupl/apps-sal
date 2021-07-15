# cook your dish here
x=int(input())
s=0
for i in range(x):
    (a, b) = map(int, input().split(' '))
    if(a>b):
        s=a
    else:
        s=b
    print(s,a+b)    
