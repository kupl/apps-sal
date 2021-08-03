from sys import*
input = stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    x = 2
    for i in range(k):
        y = x
        for j in range(k):
            print(y, end="")
            y += 1
        x += 1
        print()
