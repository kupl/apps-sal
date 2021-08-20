for _ in range(int(input())):
    k = int(input())
    x = 2
    for i in range(k):
        for j in range(k):
            print(x + j, end='')
        x = x + 1
        print()
