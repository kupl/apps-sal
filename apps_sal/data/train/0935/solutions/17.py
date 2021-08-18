n = int(input())
for i in range(n):
    a = int(input())
    if(a % 5 == 0 and a % 2 == 0):
        print(0)
    elif(a % 5 == 0 and a % 2 != 0 and a != 1):
        print(1)
    else:
        print(-1)
