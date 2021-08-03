from sys import*
input = stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    c = 0
    for i in range(n):
        d = c
        for j in range(n, 0, -1):
            if d > 0:
                print("*", end="")
                d -= 1
            else:
                print(j, end="")
        c += 1
        print()
