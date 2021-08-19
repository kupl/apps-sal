def __starting_point():
    t = int(input())
    while t:
        l = input().split(' ')
        nl = [int(i) for i in l]
        (m, n) = nl
        if m == 1 and n > 2 or (n == 1 and m > 2):
            print('No')
        else:
            print('No' if m % 2 and n % 2 else 'Yes')
        t -= 1


__starting_point()
