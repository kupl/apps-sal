n = int(input())
for i in range(n):
    a = int(input())
    for j in range(a, 0, -1):
        if j % 2 == 0:
            k = j
            while k > 0:
                print(k, end='')
                k = k - 1
            print()
        else:
            k = 1
            while k <= j:
                print(k, end='')
                k = k + 1
            print()
