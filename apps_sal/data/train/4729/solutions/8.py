DIGITS = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')


def numbers_of_letters(n):
    n_digits = ''.join((DIGITS[i] for i in map(int, str(n))))
    n = len(n_digits)
    next_n_digits = ''.join((DIGITS[i] for i in map(int, str(n))))
    result = [n_digits, next_n_digits] if n_digits != next_n_digits else [n_digits]
    while len(next_n_digits) != n:
        n = len(next_n_digits)
        next_n_digits = ''.join((DIGITS[i] for i in map(int, str(n))))
        result.append(next_n_digits)
    return result
