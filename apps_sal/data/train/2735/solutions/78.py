def jumping_number(number):
    return 'Jumping!!' if all((abs(int(str(number)[i]) - int(str(number)[i + 1])) == 1 for i in range(len(str(number)) - 1))) else 'Not!!'
