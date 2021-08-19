from collections import defaultdict


def getlist():
    return list(map(int, input().split()))


def main():
    Q = int(input())
    for i in range(Q):
        s = input()
        L = 0
        R = 0
        U = 0
        D = 0
        for j in s:
            if j == 'L':
                L += 1
            elif j == 'R':
                R += 1
            elif j == 'U':
                U += 1
            else:
                D += 1
        a = min(L, R)
        b = min(U, D)
        if a == 0 and b == 0:
            print(0)
            print('')
        elif a == 0:
            print(2)
            print('UD')
        elif b == 0:
            print(2)
            print('LR')
        else:
            ans = (a + b) * 2
            print(ans)
            seq = 'L' * a + 'D' * b + 'R' * a + 'U' * b
            print(seq)


def __starting_point():
    main()


__starting_point()
