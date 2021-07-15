# cook your dish here
n = int(input())
while n>0:
    x,y = map(int,input().strip().split())
    if x<y:
        print("<")
    elif x>y:
        print(">")
    else:
        print("=")
    n = n-1
