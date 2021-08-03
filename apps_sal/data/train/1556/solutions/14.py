t = int(input())
for i in range(0, t):
    n = int(input())
    for j in range(0, n):
        for k in range(0, n):
            if k % 2 == 0:
                print(1, end="")
            else:
                print(0, end="")
        print(" ")
