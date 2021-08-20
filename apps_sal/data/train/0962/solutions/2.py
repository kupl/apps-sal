n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
for i in a:
    for j in range(i, 0, -1):
        if j % 2 == 0:
            for k in range(j, 0, -1):
                print(k, end='')
            print()
        else:
            for k in range(1, j + 1):
                print(k, end='')
            print()
