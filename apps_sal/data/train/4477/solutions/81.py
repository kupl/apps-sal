def reverse_number(n):
    try:
        return int(str(abs(n))[::-1]) * (n // abs(n))
    except ZeroDivisionError:
        return 0
