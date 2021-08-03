class Numerical_paindrom_exception(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Not valid'


def palindrome(num):
    try:
        if type(num) != int or num < 0:
            raise Numerical_paindrom_exception
        return True if str(num)[::1] == str(num)[::-1] else False
    except Exception as e:
        return e.__str__()
