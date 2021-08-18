
for _ in range(int(input())):
    n = int(input())
    c = 1
    for i in range(n):
        for j in range(n - i):
            print(c, end="")
            c = c + 1
        print()
