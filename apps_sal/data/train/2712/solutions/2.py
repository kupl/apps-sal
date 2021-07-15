def loneliest(number):
    # Make a list of digits from the given number
    digits = []
    while number:
        number, rem = divmod(number, 10)
        digits.append(rem)

    lowest = one = float('inf')

    for i, d in enumerate(digits):
        # Calculate the range of vision for each digit
        s = sum(digits[max(0, i - d):i + d + 1]) - d

        # Update the minimums for digit 1 or the others
        if d == 1:
            one = min(one, s)
        else:
            lowest = min(lowest, s)

    # Check if 1 is the loneliest number and check if digit 1 was even in the number
    return one <= lowest and one != float('inf')

