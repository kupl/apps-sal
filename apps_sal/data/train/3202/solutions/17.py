def greet(name, owner):
    return 'Hello {}'.format({owner: 'boss'}.get(name, 'guest'))
