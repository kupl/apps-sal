def main():
    t = int(input())
    a_c = 'Chefirnemo'
    a_n = 'Pofik'
    while t:
        t -= 1
        (n, m, x, y) = list(map(int, input().split()))
        if n - 1 < x and m - 1 < y:
            print(a_n)
        elif (n - 1) % x == 0 and (m - 1) % y == 0:
            print(a_c)
        elif (n - 2) % x == 0 and (m - 2) % y == 0:
            print(a_c)
        else:
            print(a_n)


try:
    main()
except:
    pass
