def jumping_number(number):
    a12 = list(map(int, str(number)))
    if len(a12) == 1:
        return 'Jumping!!'
    else:
        for i in range(0, len(a12) - 1):
            if a12[i] + 1 == a12[i + 1] or a12[i] - 1 == a12[i + 1]:
                continue
            else:
                return 'Not!!'
        return 'Jumping!!'
