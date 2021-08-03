def is_palindrome(x): return x > 10 and str(x) == str(x)[::-1]


def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return "Not valid"

    smaller, larger = num, num

    while True:
        checks = is_palindrome(smaller), is_palindrome(larger)

        if checks == (True, False):
            return smaller
        if checks == (False, True):
            return larger
        if checks == (True, True):
            return larger

        smaller -= 1
        larger += 1
