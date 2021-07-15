def reverse_number(n):
    return ((n>0)-(n<0)) * int(str(abs(n))[::-1])

