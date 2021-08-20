def balanced_num(number):
    a = str(number)
    a = list(a)
    a = [int(x) for x in a]
    print(a)
    if len(a) < 3:
        return 'Balanced'
    if len(a) == 3 and a[0] == a[-1]:
        return 'Balanced'
    if len(a) == 3 and a[0] != a[-1]:
        return 'Not Balanced'
    if len(a) > 3:
        if len(a) % 2 == 0:
            ln = int(len(a) / 2)
            print((a[0:ln - 1], a[ln + 1:]))
            if sum(a[0:ln - 1]) == sum(a[ln + 1:]):
                return 'Balanced'
            else:
                return 'Not Balanced'
        if len(a) % 2 != 0:
            ln = int(len(a) / 2)
            print((a[0:ln], a[ln + 1:]))
            if sum(a[0:ln]) == sum(a[ln + 1:]):
                return 'Balanced'
            else:
                return 'Not Balanced'
