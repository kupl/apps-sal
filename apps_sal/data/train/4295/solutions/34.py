def balanced_num(number):
    middle = int(len(str(number)) / 2)
    left = []
    right = []
    l = []
    r = []

    if len(str(number)) == 1 or len(str(number)) == 2:
        return 'Balanced'

    elif len(str(number)) % 2 == 0:
        number = str(number)
        left = number[:middle - 1]
        right = number[middle + 1:]
        for num in left:
            l.append(int(num))
        for num in right:
            r.append(int(num))
        if sum(l) == sum(r):
            return 'Balanced'
        return 'Not Balanced'
    else:
        number = str(number)
        left = number[:middle]
        right = number[middle + 1:]
        for num in left:
            l.append(int(num))
        for num in right:
            r.append(int(num))
        if sum(l) == sum(r):
            return 'Balanced'
        return 'Not Balanced'
