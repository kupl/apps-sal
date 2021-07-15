# cook your dish here
t=int(input())
for i in range(0,t):
    a,b=(input().split())
    a=int(a)
    b=int(b)
    if(a>b):
        print(">")
    elif(a<b):
        print("<")
    elif(a==b):
        print("=")
