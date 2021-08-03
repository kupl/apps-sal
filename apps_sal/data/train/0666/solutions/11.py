for _ in range(0, int(input())):
    a = int(input())
    for i in range(1, a**2 + 1, a):
        for j in range(i, a + i):
            print(j, end="")
        print()
