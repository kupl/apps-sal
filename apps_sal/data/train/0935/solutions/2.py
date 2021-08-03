# cook your dish here
b = int(input())
for i in range(b):
    a = int(input())
    if(a % 10 == 0):
        print(0)
    elif(a % 5 == 0):
        print(1)
    else:
        print(-1)
