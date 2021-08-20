def jumping_number(n):
    n = str(n)
    if len(n) == 1:
        return 'Jumping!!'
    return 'Jumping!!' if all((abs(int(x) - int(y)) == 1 for (x, y) in zip(n[0:-1], n[1:]))) else 'Not!!'
