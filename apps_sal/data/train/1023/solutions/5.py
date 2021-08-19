for _ in range(int(input())):
    n = int(input())
    a = 0
    xx = 2
    if n == 1:
        print('1')
    elif n == 2:
        print('1')
        print('23')
    else:
        print('1')
        for _ in range(2, n):
            print(xx, end="")
            xx += 1
            if a > 0:
                print(' ' * a, end="")
            a += 1
            print(xx)
            xx += 1
        # xx+=1
        for _ in range(1, n + 1):
            print(xx, end="")
            xx += 1
        print()
