from sys import*
input = stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    x = 2
    for i in range(k):
        for j in range(k):
            print(x, end="")
            x += 2
        print()
