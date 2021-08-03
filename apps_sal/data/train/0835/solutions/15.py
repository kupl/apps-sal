t = int(input(""))
while(t):

    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    min1 = min(a, b)
    max1 = max(a, b)
    if(min1 == 1):
        if(max1 == 2):
            print("Yes")
        else:
            print("No")
    else:
        if(max1 % 2 == 0 or min1 % 2 == 0):
            print("Yes")
        else:
            print("No")
    t -= 1
