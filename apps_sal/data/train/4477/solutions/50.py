def reverse_number(n):
    num = abs(n)
    if n < 0:
        return int(str(num)[::-1]) * -1
    else:
        return int(str(num)[::-1])
