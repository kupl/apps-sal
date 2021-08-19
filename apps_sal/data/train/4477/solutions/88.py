def reverse_number(n):
    s = ''
    if n < 0:
        s = '-'
    return int(s + ''.join((i for i in reversed(str(abs(n))))))
