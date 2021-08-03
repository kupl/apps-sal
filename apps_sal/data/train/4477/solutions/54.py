def reverse_number(n):
    number = str(n)
    if n >= 0:
        number = number[::-1]
        return int(number)
    number = number[-1:0:-1]
    return int(number) * -1
