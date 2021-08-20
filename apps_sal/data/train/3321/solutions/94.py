def evil(n):
    if f'{n:b}'.count('1') % 2:
        ret = 'Odious'
    else:
        ret = 'Evil'
    return f"It's {ret}!"
