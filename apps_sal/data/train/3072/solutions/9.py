def is_narcissistic(*args):
    try:
        return all(narcissistic(int(number)) for number in args)
    except (ValueError, TypeError):
        return False


def narcissistic(number):
    n = len(str(number))
    return sum(int(digit) ** n for digit in str(number)) == number
