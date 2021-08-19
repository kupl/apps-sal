for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print('2')
    else:
        p = 2
        for i in range(n):
            for j in range(n):
                print(p, end='')
                p += 2
            print()
