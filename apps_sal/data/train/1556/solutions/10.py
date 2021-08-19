for _ in range(int(input())):
    k = int(input())
    for i in range(k):
        x = 1
        for j in range(k):
            print(x, end='')
            if x == 1:
                x = 0
            else:
                x = 1
        print()
