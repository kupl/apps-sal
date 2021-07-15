def hello(name = 'World'):
    return 'Hello, ' + (f'{name.lower().title()}!' if name else 'World!')
