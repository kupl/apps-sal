def reverse_number(n):
    return int(''.join(reversed(str(abs(n))))) * (-1 if n < 0 else 1)
