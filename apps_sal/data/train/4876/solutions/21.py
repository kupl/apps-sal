def hello(name=None):
    try:
        test = name + str(name)
        print('No Error')
    except:
        name = ''
        print('Error Handled!!!')

    if name == '' or name == None:
        new_name = 'World'
    else:
        new_name = ''
        letter = 0
        for i in name:
            if letter == 0 and i.islower:
                new_name += i.upper()
            elif letter == 0:
                new_name += i
            elif letter > 0 and i.isupper:
                new_name += i.lower()
            else:
                new_name += i

            letter += 1

    return 'Hello, ' + new_name + '!'
