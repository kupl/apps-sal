def reverse_factorial(num):
    i = 1
    while num > 1:
        i += 1
        if num % i != 0: return 'None'
        num //= i
    return f"{i}!" if num == 1 else 'None'
