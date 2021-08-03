def cookie(x):
    eaters = {str: "Zach", float: "Monica", int: "Monica"}
    try:
        return 'Who ate the last cookie? It was {}!'.format(eaters[type(x)])
    except:
        return 'Who ate the last cookie? It was the dog!'
