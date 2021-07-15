def validate(n):
    i = 0
    sum = 0
    while n:
        digit = n % 10
        n //= 10
        if i % 2 == 1:
            digit *= 2
        if digit > 9:
            digit -= 9
        sum += digit
        i += 1
    return sum % 10 == 0
