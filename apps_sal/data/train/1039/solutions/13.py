try:
    for t in range(int(input())):
        x, u = list(map(int, input().split()))
        if(x == u):
            print(0)
        elif(u > x):
            if(abs(u - x) % 2 == 0):
                if(abs(u - x) % 4 == 0):
                    print(3)
                else:
                    print(2)
            else:
                print(1)
        else:
            if(abs(x - u) % 2 != 0):
                print(2)
            else:
                print(1)


except EOFError as e:
    pass
