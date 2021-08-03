def tidyNumber(n):
    digits = list(map(int, str(n)))
    actual_digit = digits[0]

    for digit in digits[1:]:
        if digit < actual_digit:
            return False

        actual_digit = digit

    return True
