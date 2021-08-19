def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


def sol(x, y):
    return 'YES' if gcd(x, y) == 1 else 'NO'


def main():
    T = int(input())
    for i in range(T):
        (x, y) = list(map(int, input().split()))
        print(sol(x, y))


def __starting_point():
    main()


__starting_point()
