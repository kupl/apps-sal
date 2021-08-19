# cook your dish here
for i in range(int(input())):
    n = int(input())
    p = 1
    l = n - 1
    for j in range(n):
        for k in range(l):
            print(" ", end='')
        for k in range(p):
            print("*", end='')
        print()
        for k in range(l):
            print(" ", end='')
        for k in range(p):
            print("*", end='')
        print()
        p += 2
        l -= 1
