def hello(name=''):

    if not name or name == '':

        return 'Hello, World!'

    elif name:

        name = name.lower()

        return f'Hello, {name.title()}!'
