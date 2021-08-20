for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print('2')
    else:
        p = 2
        for i in range(n):
            f = p
            for j in range(n):
                print(f, end='')
                f += 1
            p += 1
            print()
