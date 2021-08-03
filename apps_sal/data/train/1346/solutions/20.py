DIVISOR = 10**9 + 7


def main():
    T = int(input())
    for t in range(T):
        N, W = list(map(int, input().split(' ')))
        if W > 8 or W < -9:
            print(0)
            continue

        if W >= 0:
            first_digits = 9 - W
        elif W < 0:
            first_digits = 10 + W

        print((first_digits * pow(10, N - 2, DIVISOR)) % DIVISOR)


main()
