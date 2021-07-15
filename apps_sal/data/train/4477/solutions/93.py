def reverse_number(n):
    n = int(str(abs(n))[::-1]) * (-1 if n < 0 else 1) 
    return n
