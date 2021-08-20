for t in range(int(input())):
    a = input().split()
    (n, month) = (int(a[0]), a[1])
    if month == 'january':
        d = n
    elif month == 'february':
        d = n + 31
    elif month == 'march':
        d = n + 60
    elif month == 'april':
        d = n + 91
    elif month == 'may':
        d = n + 121
    elif month == 'june':
        d = n + 152
    elif month == 'july':
        d = n + 182
    elif month == 'august':
        d = n + 213
    elif month == 'september':
        d = n + 244
    elif month == 'october':
        d = n + 274
    elif month == 'november':
        d = n + 305
    else:
        m = 12
        d = n + 335
    d = (d + 183) % 366
    if d == 0:
        d = 366
    if d <= 31:
        print(d, 'january')
    elif d <= 60:
        print(d - 31, 'february')
    elif d <= 91:
        print(d - 60, 'march')
    elif d <= 121:
        print(d - 91, 'april')
    elif d <= 152:
        print(d - 121, 'may')
    elif d <= 182:
        print(d - 152, 'june')
    elif d <= 213:
        print(d - 182, 'july')
    elif d <= 244:
        print(d - 213, 'august')
    elif d <= 274:
        print(d - 244, 'september')
    elif d <= 305:
        print(d - 274, 'october')
    elif d <= 335:
        print(d - 305, 'november')
    else:
        print(d - 335, 'december')
