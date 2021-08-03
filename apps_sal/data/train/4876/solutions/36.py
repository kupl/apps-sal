import string


def hello(name=''):

    if name != '':
        return ('Hello, ' + (name.lower().capitalize()) + '!')
    else:
        return ('Hello, World!')
