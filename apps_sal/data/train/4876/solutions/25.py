def hello(name=''):
    name = str(name)
    if name == 'None' or len(name) == 0 or name == ' ' * len(name):
        return 'Hello, World!'
    else:
        return f'Hello, {name.title()}!'
