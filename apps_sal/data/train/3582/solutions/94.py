# Implement String#digit? (in Java StringUtils.isDigit(String)),
# which should return true if given object is a digit (0-9), false otherwise.


def is_digit(n):
    if n.isdigit() and int(n) >= 0 and int(n) < 10:
        return True
    else:
        return False
