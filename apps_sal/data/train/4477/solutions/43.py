def reverse_number(n):
    x = int(str(abs(n))[::-1])
    return x if n>0 else -x
