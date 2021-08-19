def jumping_number(number):
    z = zip(map(int, str(number)[:-1]), map(int, str(number)[1:]))
    return ('Not', 'Jumping')[all([abs(a - b) == 1 for (a, b) in z]) or number < 10] + '!!'
