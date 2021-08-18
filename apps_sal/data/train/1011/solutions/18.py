def goodandbadPersons(n, k, s):
    if n == k:
        print('both')
    else:
        c = b = 0
        for i in s:
            if i.islower():
                c += 1
            else:
                b += 1
        if k >= c and k >= b:
            print('both')
        elif k >= b:
            print('chef')
        elif k >= c:
            print('brother')
        else:
            print('none')
    return


def __starting_point():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()
        goodandbadPersons(n, k, s)


__starting_point()
