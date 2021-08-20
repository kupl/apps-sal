def even_or_odd(n):
    if n % 2 == 0:
        return 'Even'
    elif n % 2 == 1:
        return 'Odd'
    else:
        return 'Invalid input'


a = even_or_odd(5)
print(a)
