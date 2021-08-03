res = ["Pofik", "Chefirnemo"]
for _ in range(int(input())):
    n, m, x, y = map(int, input().split())

    if n == 1 or m == 1:
        print(res[(n % x == 1 % x and m % y == 1 % y)])
    else:
        print(res[(n % x == 1 % x and m % y == 1 % y)
                  or (n % x == 2 % x and m % y == 2 % y)])
