for i in range(int(input())):
    A, B = list(map(int, input().split()))
    c = 0
    for j in range(1, A + 1):
        for k in range(1, B + 1):
            if (j + k) % 2 == 0:
                c = c + 1
    print(c)
