try:
    for _ in range(int(input())):
        k = int(input())
        for i in range(1, k + 1):
            print(" " * (k - i), end="")
            if i % 2 == 1:
                for j in range(0, i):
                    print(chr(65 + j), end="")
            else:
                for j in range(0, i):
                    print(j + 1, end="")
            print()


except:
    pass
