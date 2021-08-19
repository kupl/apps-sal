def multiply_digits(n):
    product = 1
    while n > 0:
        product *= n % 10
        n //= 10
    return product


def persistence(n):
    count = 0
    while n > 9:
        n = multiply_digits(n)
        count += 1
    return count
