def reverse_number(n):
    return -1*int(str(n*-1)[::-1]) if n<1 else int(str(n)[::-1])
