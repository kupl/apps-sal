def three_details(n):
    if n == 3:
        return 1
    if n < 5:
        return 0
    if n % 2 == 0:
        return 2 * three_details(n // 2)
    else:
        return three_details(n // 2) + three_details(n // 2 + 1)
