# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    if a>b:
        print(">")
    elif a<b:
        print("<")
    else:
        print("=")
