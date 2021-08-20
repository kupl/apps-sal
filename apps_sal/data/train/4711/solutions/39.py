def zeros(n):
    n = n // 5
    number = n
    while n != 0:
        n = n // 5
        number += n
    return number
