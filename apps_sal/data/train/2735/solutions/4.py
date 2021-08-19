def jumping_number(number):
    return 'Jumping!!' if all((abs(int(a) - int(b)) == 1 for (a, b) in zip(str(number), str(number)[1:]))) else 'Not!!'
