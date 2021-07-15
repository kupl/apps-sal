def reverse_number(n):
    if n < 0: return int(''.join([x for x in str(n)[1:][::-1]])) * -1
    else: return int(''.join([x for x in str(n)[::-1]]))
