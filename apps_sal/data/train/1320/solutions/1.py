for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print('B')
    else:
        a = n - 2
        if a == 1 or a % 2 == 0:
            print('A')
        else:
            print('B')
