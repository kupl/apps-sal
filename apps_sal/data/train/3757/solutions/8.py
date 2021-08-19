def rounding(n):
    intPart = int(n)
    fracPart = n - intPart
    if fracPart >= 0.5:
        n = intPart + 1
    else:
        n = intPart
    for i in range(6):
        up = n + i
        down = n - i
        if up % 5 == 0:
            return up
        elif down % 5 == 0:
            return down


def round_to_five(numbers):
    # your code here
    numbers = [rounding(n) for n in numbers]
    return numbers
