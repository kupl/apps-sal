def cube_odd(n):
    sum = 0
    for n in n:
        if type(n) != int:
            return None
        if n % 2 != 0:
            sum += n**3
    return sum
