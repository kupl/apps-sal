def jumping_number(number):
    ls = list(map(int, str(number)))
    for i in range(len(ls) - 1):
        if ls[i + 1] != ls[i] + 1 and ls[i + 1] != ls[i] - 1:
            return 'Not!!'
    return 'Jumping!!'
