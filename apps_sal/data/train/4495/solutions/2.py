def am_I_afraid(day, x):
    return {'Mo': x       == 12,
            'Tu': x       >  95,
            'We': x       == 34,
            'Th': x       ==  0,
            'Fr': x % 2   ==  0,
            'Sa': x       == 56,
            'Su': abs(x)  == 666}[day[:2]]
