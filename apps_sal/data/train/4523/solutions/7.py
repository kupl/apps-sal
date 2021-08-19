def solve(n):
    total = sum_digit(n)
    largest = n
    i = 1
    while n > 0:
        n = n - n % 10 ** i - 1
        print(n)
        new_total = sum_digit(n)
        i += 1
        if new_total > total:
            total = new_total
            largest = n
    return largest


def sum_digit(num):
    tot = 0
    while num > 0:
        tot += num % 10
        num = int(num / 10)
    return tot
