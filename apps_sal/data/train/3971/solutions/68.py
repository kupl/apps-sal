def tidyNumber(n):
    digits = []
    while n > 0:
        digit = n % 10
        n = n // 10
        digits.append(digit)
    tidy = True
    i = 1
    while i < len(digits):
        if digits[i] > digits[i - 1]:
            tidy = False
            break
        i = i + 1
    return tidy
