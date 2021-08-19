def hello(*name):
    if name:
        if name[0]:
            return 'Hello, ' + name[0].title() + '!'
        else:
            return 'Hello, World!'
    else:
        return 'Hello, World!'
