def jumping_number(number):
    l = [int(i) for i in str(number)]
    if len(l) == 1:
        return 'Jumping!!'
    prev = l[0] - 1
    for i in l:
        if abs(i - prev) != 1:
            return 'Not!!'
        prev = i
    return 'Jumping!!'
