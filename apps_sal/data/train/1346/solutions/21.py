DIVISOR = 10 ** 9 + 7


def main():
    power_of_9s = [10 ** n % DIVISOR for n in range(1001)]
    T = int(input())
    for t in range(T):
        (N, W) = list(map(int, input().split(' ')))
        if W > 8 or W < -9:
            print(0)
            continue
        if W >= 0:
            first_digits = 9 - W
        elif W < 0:
            first_digits = 10 + W
        mid_digits = power_of_9s[N - 2]
        print(first_digits * mid_digits % DIVISOR)


main()
