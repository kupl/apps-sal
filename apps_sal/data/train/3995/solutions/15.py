def dating_range(age, x=2, y=7, z=.1):
    return f'{age // x + y}-{x * (age - y)}' if age > x * y else f'{int(age * (1 - z))}-{int(age * (1 + z))}'
