# cook your dish here
for _ in range(int(input())):
    n = int(input())
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(j, end="")
            print(i, end="")
        print()
