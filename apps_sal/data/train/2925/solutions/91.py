def get_digit_count(n):
    digits = 0
    while 0 < n:
        n //= 10
        digits += 1
    return digits

def multiply(n):
    return n * (5**get_digit_count(abs(n)))
