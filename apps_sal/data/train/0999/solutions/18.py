t = int(input())
while t:
    t -= 1
    k = int(input())
    for i in range(1, k + 1):
        for j in range(k - i):
            print(' ', end='')
        for j in range(i):
            if i % 2 == 1:
                print(chr(65 + j), end='')
            else:
                print(j + 1, end='')
        print()
