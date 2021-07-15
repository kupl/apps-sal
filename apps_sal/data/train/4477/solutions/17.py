def reverse_number(n):
    return int('-' * (n < 0) + ''.join(reversed(str(abs(n)))))
