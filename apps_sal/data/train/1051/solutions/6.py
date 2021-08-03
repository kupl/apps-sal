for i in range(int(input())):
    s = int(input())
    for i in range(0, s + 1):
        for k in range(i):
            print("*", end="")
        print(i)
