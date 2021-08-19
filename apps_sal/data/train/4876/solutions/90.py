def hello(name='World'):
    if name in ('', ' '):
        name = 'World'
    return f'Hello, {name.title()}!'
