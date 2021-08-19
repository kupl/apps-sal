# cook your dish here
for i in range(int(input())):
    n = int(input())
    for j in range(n, -1, -1):
        temp = j
        for k in range(temp, 0, -1):
            print(" ", end="")
            temp -= 1
        temp2 = j
        for l in range(n, temp2 - 1, -1):
            print(l, end="")
        print()
    for m in range(1, n + 1):
        for i in range(m):
            print(" ", end="")
        for o in range(n, m - 1, -1):
            print(o, end="")
        print("")
