t = int(input())
for _ in range(t):
    x, y = list(map(int, input().split()))
    if(x > y):
        if(abs(x - y) % 2 == 0):
            print(1)
        else:
            print(2)
    elif(x < y):
        if(abs(x - y) % 2 != 0):
            print(1)
        elif(abs(x - y) % 2 == 0 and abs(x - y) % 4 != 0):
            print(2)
        else:
            print(3)
    else:
        print(0)
