n = int(input())
l = [0] * n
for x in range(n):
    l[x] = int(input())
for i in range(n):
    z = 2
    for j in range(1, l[i] + 1):
        for k in range(1, l[i] + 1):
            print(z, end='')
            z += 2
        print()
