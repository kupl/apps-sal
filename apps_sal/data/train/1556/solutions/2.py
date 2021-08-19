for _ in range(0, int(input())):
    a = int(input())
    for i in range(0, a):
        for j in range(0, a):
            if j % 2 == 0:
                print(1, end='')
            else:
                print(0, end='')
        print()
