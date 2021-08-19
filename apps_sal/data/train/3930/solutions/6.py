def dollar_to_speech(value):
    if '-' in value:
        return 'No negative numbers are allowed!'
    else:
        a = value.replace('$', '').split('.')
        if int(a[0]) > 1 and int(a[1]) > 1:
            return '{} dollars and {} cents.'.format(int(a[0]), int(a[1]))
        elif int(a[0]) == 1 and int(a[1]) == 1:
            return '{} dollar and {} cent.'.format(int(a[0]), int(a[1]))
        elif int(a[0]) < 1 and int(a[1]) < 1 or (int(a[0]) > 1 and int(a[1]) < 1):
            return '{} dollars.'.format(int(a[0]))
        elif int(a[0]) == 1 and int(a[1]) < 1:
            return '{} dollar.'.format(int(a[0]))
        elif int(a[0]) > 1 and int(a[1]) == 1:
            return '{} dollars and {} cent.'.format(int(a[0]), int(a[1]))
        elif int(a[0]) == 1 and int(a[1]) > 1:
            return '{} dollar and {} cents.'.format(int(a[0]), int(a[1]))
        elif int(a[1]) > 1:
            return '{} cents.'.format(int(a[1]))
        else:
            return '{} cent.'.format(int(a[1]))
