def jumping_number(number):
    a = []
    if number < 10:
        return 'Jumping!!'
    for i in str(number):
        a.append(int(i))
    for i in range(1, len(a)):
        if a[i - 1] - a[i] == 1 or a[i - 1] - a[i] == -1:
            pass
        else:
            return 'Not!!'
    return 'Jumping!!'
