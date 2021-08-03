def faulty_odometer(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10

    result = 0
    count = len(digits)
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] >= 5:
            digits[i] -= 1
        result += digits[i] * 9**(count - 1)
        count -= 1
    return result
