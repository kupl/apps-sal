t = int(input())
for i in range(t):
    k = int(input())
    for j in range(k, 0, -1):
        if j % 2 == 0:
            for m in range(j, 0, -1):
                print(m, end='')
        else:
            for m in range(1, j + 1):
                print(m, end='')
        print()
