# cook your dish here
for _ in range(int(input())):
    k = int(input())
    x = 0
    for i in range(k):
        y = x
        for j in range(k):
            print(y, end='')
            if y == 0:
                y = 1
            else:
                y = 0
        if x == 0:
            x = 1
        else:
            x = 0
        print()
