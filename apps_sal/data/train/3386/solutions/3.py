from string import ascii_uppercase


def get_column_title(n):
    n -= 1
    result = []
    while n >= 0:
        result.append(ascii_uppercase[n % 26])
        n = n // 26 - 1
    if not result:
        raise ValueError('Not a valid number.')
    return ''.join(result[::-1])
