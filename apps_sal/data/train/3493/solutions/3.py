def change_count(change):
    a = change.split(' ')
    L = []
    for i in range(len(a)):
        if a[i] == 'penny':
            L.append(0.01)
        elif a[i] == 'nickel':
            L.append(0.05)
        elif a[i] == 'dime':
            L.append(0.1)
        elif a[i] == 'quarter':
            L.append(0.25)
        elif a[i] == 'dollar':
            L.append(1.0)
    b = sum(L)
    x = round(b + 1e-07, 2)
    a = '$' + '%.2f' % x
    y = a.split()
    if len(y) == 4:
        y.append('0')
        return sum(y)
    else:
        return a
