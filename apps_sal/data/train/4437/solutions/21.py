def cookie(x):
    choice = {str: 'Zach', int: 'Monica', float: 'Monica'}
    return f'Who ate the last cookie? It was {choice.get(type(x), "the dog")}!'
