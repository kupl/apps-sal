# cook your dish here
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if(a < b):
        print("<")
    elif(a > b):
        print(">")
    else:
        print("=")
