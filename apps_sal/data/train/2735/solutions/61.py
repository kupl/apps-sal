def jumping_number(n):
    return 'Jumping!!' if all((int(a) - int(b))**2 == 1 for a, b in zip(str(n), str(n)[1:])) else 'Not!!'
