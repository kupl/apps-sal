for i in range(int(input())):
    n = int(input())
    if n % 5 == 0:
        if n % 10 == 0:
            print(0)
        else:
            print(1)
    else:
        print((-1))  # cook your dish here
