for i in range(int(input())):
    s = int(input())
    for i in range(s):
        for k in range(i):
            print("*", end="")
        for j in range(i, s):
            print(s - j, end="")
        print()  # cook your dish here
